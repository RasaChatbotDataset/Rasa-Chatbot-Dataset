import zipfile
import ast
import os
import pandas as pd
from dotenv import dotenv_values
import requests
import time
import json
import argparse

config = dotenv_values('config.env')
FILES = [os.path.join('results', '06_results', 'chatbots_sfsd.csv'), os.path.join('results', '06_results', 'chatbots_mfsd.csv'), os.path.join('results', '06_results', 'chatbots_sfmd.csv'), os.path.join('results', '06_results', 'chatbots_mfmd.csv')]
RESULTS_FOLDER = os.path.join('results', '18_results')
INPUT_FILE = os.path.join('results', '17_results', '3_chatbots.csv')
CHATBOT_FILE = 'chatbots.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
JSON_FOLDER = os.path.join('results', '01_results', 'repositories_json')
TOPICS_FILE_NAME = '18_topic_categories.csv'


# Query OpenAI ChatGPT
def query_chatgpt(prompt, parameters):

    headers = {
        "Content-Type": "application/json",
        "api-key": parameters['API_KEY'],
    }
    payload = {
    "messages": [
        {
        "role": "system",
        "content": [{"type": "text", "text": prompt}]
        }
    ],
    "temperature": parameters['TEMPERATURE'],
    "top_p": parameters['TOP_P'],
    "max_tokens": 800
    }

    response = requests.post(parameters['ENDPOINT'], headers=headers, json=payload)
    
    return response

def query_gemini(prompt, parameters):

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": parameters['API_KEY'],
    }

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ]}

    response = requests.post(parameters['ENDPOINT'], headers=headers, json=payload)
   
   # response = parameters['CLIENT'].models.generate_content(
    #    model="gemini-2.5-flash",
     #   contents=prompt,
    #)

    return response


# Extract topic from file
def extract_topic(chatbot, topics, llm,  parameters, response_folder):
    
    # Readme files
    readme_merge = ""
    file_list = ast.literal_eval(chatbot['readme-files'])
    zip_path = os.path.join(ZIP_FOLDER, chatbot['full-name'].replace('/', '_') + '.zip')
    repository =  zipfile.ZipFile(zip_path, 'r')

    for file in file_list:
        full_path = chatbot['full-name'].split('/')[-1]+'-'+chatbot['last-commit']+ '/' + file
        # Open file
        with repository.open(full_path) as f:
            try:
                # Decode file
                content = f.read().decode()
                readme_merge = readme_merge + content

            except UnicodeDecodeError as e:
                print(f"Decode error")

    # Repository description
    repo_json_file = os.path.join(JSON_FOLDER, chatbot['full-name'].replace('/', '_') + '.json')
    f = open(repo_json_file)
    json_repo = json.load(f)
    description = json_repo['description']
    chatbot['entities'] = ast.literal_eval(chatbot['entities'])
    chatbot['slots'] = ast.literal_eval(chatbot['slots'])
    retrieval_components = list(set(chatbot['entities']+chatbot['slots']))

    # Prompt definition
    prompt = f"""Your task is to extract the topic/category of a Rasa chatbot. Given:
                - the repository name: {chatbot['full-name'].split('/')[-1]}
                - the description: {description}
                - the README: {readme_merge}
                - the list of intents: {chatbot['intents']}
                - the list of entities: {retrieval_components}
                - the list of actions: {chatbot['actions']}
                Select the topic of the chatbot considering this list of topics: {topics}. If the chatbot's topic matches one of these, use the topic in the list. Otherwise define a new topic. 
                Answer only with the topic, with no further words."""

    # Ask LLM to extract services from file
    if llm == 'OPENAI':
        response = query_chatgpt(prompt, parameters)
    elif llm == 'GEMINI':
        response = query_gemini(prompt, parameters)
    
    n_retry = 0
    while response.status_code == 429 and n_retry < 5:
        print("Error 429: too many requests")
        time.sleep(30)
        if llm == 'OPENAI':
            response = query_chatgpt(prompt, parameters)
        elif llm == 'GEMINI':
            response = query_gemini(prompt, parameters)
        n_retry += 1
    if n_retry == 5:
        return -1

    # Parse response
    json_response = response.json()
    if llm == 'OPENAI':
        topic = json_response['choices'][0]['message']['content'].strip()
    elif llm == 'GEMINI':
        topic = json_response['candidates'][0]['content']['parts'][0]['text'].strip()

    # Save request and response
    r_file = os.path.join(response_folder, chatbot['id'].replace('/', '_') + '.txt')
    response_file = open(r_file, 'w', encoding="utf-8", errors="replace")
    response_file.write('REQUEST\n' + prompt + '\n\nRESPONSE\n' + topic)
    response_file.close()

    return topic
      

def main():
    
    # Optional argument for number of chatbots
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument(
        "--n-chatbots",
        type=int,
        default=-1,
        help="Number of chatbots (default: all)"
    )

    args = parser.parse_args()

    print('\n\n', '-'*20, 'TOPIC EXTRACTION', '-'*20, '\n') 

    # LLM configuration
    # Gemini
    if config['LLM'] == 'GEMINI':
        if not config['LLM_ENDPOINT'] or not config['LLM_KEY']:
            print('Incorrect GEMINI configuration in file config.env')
            exit()

        parameters = {
                        'ENDPOINT' : config['LLM_ENDPOINT'],
                        'API_KEY' : config['LLM_KEY']
                    }
        LLM_RESPONSE_FOLDER = os.path.join(RESULTS_FOLDER, 'gemini_responses')
        print('LLM: Google Gemini')

    # ChatGPT
    elif config['LLM'] == 'OPENAI':
        if not config['LLM_ENDPOINT'] or not config['LLM_KEY']:
            print('Incorrect OPENAI configuration in file config.env')
            exit()
        parameters = {
                        'TEMPERATURE' : 1,
                        'TOP_P' : 0.15,
                        'ENDPOINT' : config['LLM_ENDPOINT'],
                        'API_KEY' : config['LLM_KEY']
                    }
        LLM_RESPONSE_FOLDER = os.path.join(RESULTS_FOLDER, 'chatgpt_responses')
        print('LLM: OpenAI GPT')

    else:
       print('Incorrect LLM value in file config.env') 
       exit()
    
    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)
    if not os.path.isdir(LLM_RESPONSE_FOLDER):
        os.mkdir(LLM_RESPONSE_FOLDER)

    # Join chatbot files
    chatbots = pd.read_csv(INPUT_FILE, sep=CSV_SEPARATOR)
    cb_files = pd.DataFrame()

    # Chatbot number check
    if args.n_chatbots >0 and args.n_chatbots < chatbots.shape[0]:
        chatbots = chatbots.head(args.n_chatbots)
        print(f'Number of chatbots: {args.n_chatbots}\n')
    else:
        print(f'Number of chatbots: {chatbots.shape[0]} (all)\n')

    for file in FILES:
        cb_with_files = pd.read_csv(file, sep=CSV_SEPARATOR)
        cb_with_files = cb_with_files[['id', 'n-readme-files', 'readme-files']]
        cb_files = pd.concat([cb_files, cb_with_files])

    chatbots = pd.merge(chatbots, cb_files, how='inner')

    chatbots.to_csv(os.path.join(RESULTS_FOLDER, 'chatbots_join_readme.csv'), sep=CSV_SEPARATOR, index=False)

    # Set TOPICS
    topics_file = open(TOPICS_FILE_NAME, 'r', encoding='utf-8')
    topics = topics_file.read().split(CSV_SEPARATOR)
    


    # Add columns
    chatbots['topic'] = None
    
    for index, chatbot in chatbots.iterrows():

        if index%10==0:
            print(f'> Processed chatbots: {index}/{chatbots.shape[0]}')

        # Extract topic
        topic = extract_topic(chatbot, topics, config['LLM'], parameters, LLM_RESPONSE_FOLDER)
        if topic == -1:
            break
        chatbots.at[index, 'topic'] = topic

    print(f'> Processed chatbots: {chatbots.shape[0]}/{chatbots.shape[0]}')
    
    # Drop columns
    chatbots = chatbots.drop('n-readme-files', axis=1)
    chatbots = chatbots.drop('readme-files', axis=1)

    chatbots.to_csv(os.path.join(RESULTS_FOLDER, CHATBOT_FILE), sep=CSV_SEPARATOR, index=False)
    print('Step 18 completed\n')
    print('CONGRATULATIONS: YOUR BRASATO IS READY')



main()