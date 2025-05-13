import zipfile
import ast
import os
import pandas as pd
from dotenv import dotenv_values
import requests
import time
import json
import csv

TEMPERATURE = 1
TOP_P = 0.15

config = dotenv_values('config.env')

FILES = ['results/08_results/chatbot_repositories_sfsd.csv', 'results/08_results/chatbot_repositories_mfsd.csv', 'results/08_results/chatbot_repositories_sfmd.csv', 'results/08_results/chatbot_repositories_mfmd.csv']
RESULTS_FOLDER = 'results/20_results/'
CHATGPT_RESPONSE_FOLDER = RESULTS_FOLDER +'/chatgpt_responses'
INPUT_FILE = 'results/19_results/3_chatbots.csv'
CHATBOT_FILE = 'chatbots.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
JSON_FOLDER = 'results/01_results/repositories_json/'
TOPICS_FILE_NAME = '20_topic_categories.csv'


# Query OpenAI ChatGPT
def query_chatgpt(prompt):
    print("sending request")

    API_KEY = config['OPENAI_KEY']
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    payload = {
    "messages": [
        {
        "role": "system",
        "content": [{"type": "text", "text": prompt}]
        }
    ],
    "temperature": TEMPERATURE,
    "top_p": TOP_P,
    "max_tokens": 800
    }
    ENDPOINT = config['OPENAI_ENDPOINT']

    response = requests.post(ENDPOINT, headers=headers, json=payload)
    
    return response


# Extract topic from file
def extract_topic(chatbot, topics):
    
    # Readme files (exclude rasa hq base one)
    readme_merge = ""
    file_list = ast.literal_eval(chatbot['readme-files'])
    zip_path = ZIP_FOLDER + '/' + chatbot['full-name'].replace('/', '_') + '.zip'
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
    repo_json_file = JSON_FOLDER + chatbot['full-name'].replace('/', '_') + '.json'
    f = open(repo_json_file)
    json_repo = json.load(f)
    description = json_repo['description']
    chatbot['entities'] = ast.literal_eval(chatbot['entities'])
    chatbot['slots'] = ast.literal_eval(chatbot['slots'])
    retrieval_components = list(set(chatbot['entities']+chatbot['slots']))

    prompt = f"""Your task is to extract the topic/category of a Rasa chatbot. Given:
                - the repository name: {chatbot['full-name'].split('/')[-1]}
                - the description: {description}
                - the README: {readme_merge}
                - the list of intents: {chatbot['intents']}
                - the list of entities: {retrieval_components}
                - the list of actions: {chatbot['actions']}
                Select the topic of the chatbot considering this list of topics: {topics}. If the chatbot's topic matches one of these, use the topic in the list. Otherwise define a new topic. 
                Answer only with the topic, with no further words."""

    # Ask chatgpt to extract services from file
    response = query_chatgpt(prompt)
    n_retry = 0
    while response.status_code == 429 and n_retry < 5:
        print("Error 429: too many requests")
        time.sleep(30)
        response = query_chatgpt(prompt)
        n_retry += 1
    if n_retry == 5:
        return -1

    # Parse response
    json_response = response.json()
    topic = json_response['choices'][0]['message']['content'] #"NO\n\nPurpose of external services"#

    # Save request and response
    r_file = CHATGPT_RESPONSE_FOLDER + '/' + chatbot['id'].replace('/', '_') + '.txt'
    response_file = open(r_file, 'w', encoding="utf-8", errors="replace")
    response_file.write('REQUEST\n' + prompt + '\n\nRESPONSE\n' + topic)
    response_file.close()

    print(topic)
    return topic
      

def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)
    if not os.path.isdir(CHATGPT_RESPONSE_FOLDER):
        os.mkdir(CHATGPT_RESPONSE_FOLDER)

    # Join chatbot files
    chatbots = pd.read_csv(INPUT_FILE, sep=CSV_SEPARATOR)
    cb_files = pd.DataFrame()

    for file in FILES:
        cb_with_files = pd.read_csv(file, sep=CSV_SEPARATOR)
        cb_with_files = cb_with_files[['id', 'n-readme-files', 'readme-files']]
        cb_files = pd.concat([cb_files, cb_with_files])

    chatbots = pd.merge(chatbots, cb_files, how='inner')

    chatbots.to_csv(RESULTS_FOLDER + 'chatbots_join_readme.csv', sep=CSV_SEPARATOR, index=False)

    # Set TOPICS
    topics_file = open(TOPICS_FILE_NAME, 'r', encoding='utf-8')
    topics = topics_file.read().split(CSV_SEPARATOR)
    


    # Add columns
    chatbots['topic'] = None
    
    for index, chatbot in chatbots.iterrows():

        print(chatbot['id'])

        # Extract topic
        topic = extract_topic(chatbot, topics)
        if topic== -1:
            break
        chatbots.at[index, 'topic'] = topic

    
    # Drop columns
    chatbots = chatbots.drop('n-readme-files', axis=1)
    chatbots = chatbots.drop('readme-files', axis=1)

    chatbots.to_csv(RESULTS_FOLDER +CHATBOT_FILE, sep=CSV_SEPARATOR, index=False)



main()