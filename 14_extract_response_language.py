import detectlanguage
import yaml
import json
import zipfile
import ast
import os
import re
from dotenv import dotenv_values
import random
import csv

config = dotenv_values('config.env')
detectlanguage.configuration.api_key = config['DETECT_LANGUAGE_KEY']

INPUT_FILE = 'results/13_results/chatbots.csv'
RESULTS_FOLDER = 'results/14_results/'
CHATBOT_FILE = RESULTS_FOLDER + 'chatbots.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'


# Extract language from domain file
def extract_response_language(chatbot):


    zip_path = ZIP_FOLDER + '/' + chatbot['full-name'].replace('/', '_') + '.zip'

    repository =  zipfile.ZipFile(zip_path, 'r')

    file_list = ast.literal_eval(chatbot['domain-files'])
    languages = []

    for file in file_list:
        file_languages = extract_response_language_from_file(chatbot, file, repository)

        for l in file_languages:
            if l not in languages:
                languages.append(l)

    return languages


# Extract response language from single file
def extract_response_language_from_file(chatbot, file, repository):

    languages = []

    default_responses = ['utter_iamabot', 'utter_greet', 'utter_goodbye']
    full_config_path = chatbot['full-name'].split('/')[-1]+'-'+chatbot['last-commit']+ '/' + file

    # Open file
    with repository.open(full_config_path) as nlu_file:
        try:
            # Decode file
            content = nlu_file.read().decode()
            domain = yaml.safe_load(content)

            if 'responses' in domain and domain['responses']: 
                responses = domain['responses']
            elif 'templates' in domain and len(domain['templates']) > 0:
                responses = domain['templates']
            else:
                return languages
            
            # Default responses cleaning
            for default_response in default_responses:
                if len(responses) <= 2:
                    break

                if default_response in responses.keys():
                    del responses[default_response]

            # Responses selection
            phrases_sample = []
            possible_keys = list(responses.keys())

            while len(possible_keys) > 0 and len(phrases_sample) < 2:
                random_key = random.choice(list(possible_keys))
                response_text = ""
                for response in responses[random_key]:

                    # Responses as string
                    if isinstance(response, str):
                        response_text += re.sub(r'[\{].*?[\}]', '', response).replace('\n-', ' ')
                    # Responses as dict [text: string]
                    else:
                        # Response of type text
                        if 'text' in response:
                            # Field text in response is a string
                            if isinstance(response['text'], str):
                                response_text += re.sub(r'[\{].*?[\}]', '', response['text']).replace('\n-', ' ')
                            # Field text in response is a list
                            else:
                                for t in response['text']:
                                    response_text += re.sub(r'[\{].*?[\}]', '', t).replace('\n-', ' ')
                        
                        # Response of type custom: unknown structure, ignore
                        elif 'custom' in response:
                            break

                        elif isinstance(response, list):
                            for t in response:
                                response_text += re.sub(r'[\{].*?[\}]', '', t).replace('\n-', ' ')

                    if response_text != '':
                        # Append response sample
                        phrases_sample.append(response_text)
               
                possible_keys.remove(random_key)
       
            if len(responses) == 0:
                return languages
            
            # Detect language of sample responses
            lang_response = detectlanguage.detect(phrases_sample)
            
            for lang in lang_response:
                if lang and lang[0]['language'] not in languages:
                    languages.append(lang[0]['language'])

        except UnicodeDecodeError as e:
            print(f"Decode error")
        except yaml.YAMLError as e:
            print("Yaml parsing error")
        except Exception as e:
            print(f"Exception: {e}")
    

    return languages


           

def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open files
    csv.field_size_limit(100000000)
    chatbot_file = open(INPUT_FILE, 'r', encoding="utf-8")
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    result_file = open(CHATBOT_FILE, 'w', newline='')
    header = reader.fieldnames + ['response-languages']
    writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=header)
    writer.writeheader()
    

    for chatbot in chatbots:

        print(chatbot['full-name'])
            
        # Check API limit
        language_api_status = detectlanguage.user_status()
        if language_api_status['requests'] == language_api_status['daily_requests_limit'] or language_api_status['bytes'] > language_api_status['daily_bytes_limit'] - 10000:
            print('Detect language API daily limit exceeded')
            break

        chatbot['response-languages'] = None

        # Extract response language
        response_language = extract_response_language(chatbot)
        if len(response_language) > 0:
            chatbot['response-languages'] = response_language


        # Write chatbot        
        writer.writerow(chatbot)

    # Close files
    chatbot_file.close()
    result_file.close()



main()