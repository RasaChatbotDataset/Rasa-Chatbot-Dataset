import zipfile
import ast
import os
import pandas as pd
from dotenv import dotenv_values
import requests
import time
import re

TEMPERATURE = 1
TOP_P = 0.15

config = dotenv_values('config.env')

FILES = ['results/08_results/chatbot_repositories_sfsd.csv', 'results/08_results/chatbot_repositories_mfsd.csv', 'results/08_results/chatbot_repositories_sfmd.csv', 'results/08_results/chatbot_repositories_mfmd.csv']
RESULTS_FOLDER = 'results/18_results/'
CHATGPT_RESPONSE_FOLDER = RESULTS_FOLDER +'/chatgpt_responses'
INPUT_FOLDER = 'results/17_results/'
CHATBOT_FILE = 'chatbots.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'


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


# Ask chatgpt to merge 10 responses
def merge_responses(chatbot_id, responses, n_file, file_content, file_type):
    services = [] 
    
    s = '\n'.join(responses)

    # Select prompt (actions or readme file)
    if file_type == 'actions':
        prompt = f'''Problem: This is a python actions.py file of Rasa chatbot {file_content} 
        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        '''
    else:
        prompt = f'''Problem: This is a README file from a Rasa chatbot repository {file_content}
        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        '''
    
    # Complete prompt
    prompt += f'''
    For this problem I received these answers, each with a list of services:
    {s}
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else'''

    # Send query
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
    content = json_response['choices'][0]['message']['content']#"NO\n\nPurpose of external services"#

    # Create result folder
    if not os.path.isdir(CHATGPT_RESPONSE_FOLDER + '/' + chatbot_id.replace('/', '_')):
        os.mkdir(CHATGPT_RESPONSE_FOLDER + '/' + chatbot_id.replace('/', '_'))

    # Save request and response
    r_file = CHATGPT_RESPONSE_FOLDER + '/' + chatbot_id.replace('/', '_') + '/' + file_type + '_' + str(n_file) + '.txt'
    response_file = open(r_file, 'w', encoding="utf-8", errors="replace")
    response_file.write('REQUEST\n' + prompt + '\n\nRESPONSE\n' + content)
    response_file.close()

    # Parse services list
    if not content.startswith('NO'):
        external_services = re.split('Purpose of External Services', content, flags=re.IGNORECASE)[0].replace('#', '').replace('*', '').strip().replace('\n', ',')
        services = external_services.replace(', ', ',').split(',')

    return services



# Extract services lost from file (10 requests + 1 merge)
def extract_services_from_file(chatbot, repository, file, file_type, n_file):
    services = []
    merged_services = []

    full_path = chatbot['full-name'].split('/')[-1]+'-'+chatbot['last-commit']+ '/' + file

    # Open file
    with repository.open(full_path) as f:
        try:
            # Decode file
            content = f.read().decode()

            # Select prompt (readme prompt or actions prompt)
            if file_type == 'actions':
                prompt = f"""This is a python actions.py file of Rasa chatbot: {content}
                Does the chatbot use any database (local or external) or any external service?\
                Begin the answer with YES if it does or NO if it doesn't, a list of these databases and services (only names on a single line, no further explanation, no numeration)\
                and in a new section titled \"Purpose of external services\" explain the purpose of each service."""
            else:
                prompt = f"""This is a README file from a Rasa chatbot repository: {content} 
                Does the described chatbot use any database (local or external) or any external service?\
                Begin the answer with YES if it does or NO if it doesn't, a list of these databases and services (only names on a single line, no further explanation, no numeration)\
                and in a new section titled \"Purpose of external services\" explain the purpose of each service. """

            # Extract services 10 times
            for i in range(10):

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
                resp_content = json_response['choices'][0]['message']['content'] #"NO\n\nPurpose of external services"#

                if resp_content.startswith('YES'):
                    resp_content = resp_content.replace('YES', '', 1)
                    external_services = re.split('Purpose of External Services', resp_content, flags=re.IGNORECASE)[0].strip('\n').strip().strip(':').replace('\n', ',')
                    services.append(external_services)
                    print('\n\nSERVICES '+str(services))
                else:
                    services.append('None')

            
            # Merge responses
            merged_services = merge_responses(chatbot['id'], services, n_file, content, file_type)

        except UnicodeDecodeError as e:
            print(f"Decode error")

    return merged_services


# Extract services from files
def extract_services_from_files(chatbot, file_type, file_list):

    external_services = []

    zip_path = ZIP_FOLDER + '/' + chatbot['full-name'].replace('/', '_') + '.zip'
    repository =  zipfile.ZipFile(zip_path, 'r')

    # For each file
    for i in range(len(file_list)):
        
        # Extract service 
        services = extract_services_from_file(chatbot, repository, file_list[i], file_type, i)
        if services == -1:
            return -1, -1

        # Append services
        external_services = external_services + services
    
    return external_services

      

def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)
    if not os.path.isdir(CHATGPT_RESPONSE_FOLDER):
        os.mkdir(CHATGPT_RESPONSE_FOLDER)

    # Join chatbot files
    chatbots = pd.read_csv(INPUT_FOLDER + CHATBOT_FILE, sep=CSV_SEPARATOR)
    cb_files = pd.DataFrame()

    for file in FILES:
        cb_with_files = pd.read_csv(file, sep=CSV_SEPARATOR)
        cb_with_files = cb_with_files[['id', 'n-readme-files', 'readme-files', 'actions-files']]
        cb_files = pd.concat([cb_files, cb_with_files])

    chatbots = pd.merge(chatbots, cb_files, how='inner')

    chatbots.to_csv(RESULTS_FOLDER + 'chatbots_join_files.csv', sep=CSV_SEPARATOR, index=False)

    # Add columns
    chatbots['external-services-actions'] = None
    chatbots['n-external-services-actions'] = None
    chatbots['external-services-readme'] = None
    chatbots['n-external-services-readme'] = None
    
    for index, chatbot in chatbots.iterrows():
        print(chatbot['id'])

        # Extract services from action files
        if int(chatbot['n-actions-files']) > 0 :
            file_list = ast.literal_eval(chatbot['actions-files'])
            external_services = extract_services_from_files(chatbot, 'actions', file_list)
            if external_services == -1:
                break
            chatbots.at[index, 'external-services-actions'] = external_services
            chatbots.at[index, 'n-external-services-actions'] = len(external_services)

        # Extract services from readme files
        if int(chatbot['n-readme-files']) > 0 :
            file_list = ast.literal_eval(chatbot['readme-files'])   
            external_services = extract_services_from_files(chatbot, 'readme', file_list)
            if external_services == -1:
                break
            chatbots.at[index, 'external-services-readme'] = external_services
            chatbots.at[index, 'n-external-services-readme'] = len(external_services)
    
    # Drop columns
    chatbots = chatbots.drop('n-readme-files', axis=1)
    chatbots = chatbots.drop('readme-files', axis=1)
    chatbots = chatbots.drop('n-actions-files', axis=1)
    chatbots = chatbots.drop('actions-files', axis=1)
    chatbots.to_csv(RESULTS_FOLDER +CHATBOT_FILE, sep=CSV_SEPARATOR, index=False)



main()