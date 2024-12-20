import requests
import zipfile
import yaml
import ast
import detectlanguage
import csv
from dotenv import dotenv_values
import re
import random

config = dotenv_values('config.env')

KEYWORDS  = ['intents']

REPOSITORIES_FILE = 'repositories.csv'
CHATBOTS_FILE = 'chatbots - Copia.csv'
CSV_SEPARATOR= ';'

REPOSITORY = 'MainP0k/Bot_Rasa'
detectlanguage.configuration.api_key = config['DETECT_LANGUAGE_KEY']
  

def download_zip(repo_name, branch):
    download_url = f"https://github.com/{repo_name}/archive/refs/heads/{branch}.zip"
    print(download_url)
    
    response = requests.get(download_url)
    if response.status_code != 200:
        print(f'Error in repository {repo_name} ZIP download: {response.status_code}')
        return -1
    else:
        zip_path = f"{repo_name.replace('/', '_')}.zip"
        with open(zip_path, "wb") as f:
            f.write(response.content)
        return zip_path
    
    

def analyze_repository(zip_path, repo_info):
    repository =  zipfile.ZipFile(zip_path, 'r')
    
    file_list = repository.namelist()
    chatbot_info = {}
    chatbot_info['n_entities'] = []
    chatbot_info['n_actions'] = []
    chatbot_info['n_intents'] = []
    chatbot_info['n_slots'] = []
    chatbot_info['entities'] = []
    chatbot_info['actions'] = []
    chatbot_info['intents'] = []
    chatbot_info['slots_complete'] = []
    chatbot_info['slot_names'] = []
    chatbot_info['entity_types'] = []
    chatbot_info['version'] = []
    chatbot_info['training_phrases_language']= []
    chatbot_info['responses_language']= []



    # Domain information
    for domain_file_path in repo_info['domain-files']:
        complete_domain_path = repo_info['full-name'].split('/')[1] + '-'+repo_info['default-branch']+'/' + domain_file_path

        if complete_domain_path in file_list:
            chatbot_info = extract_domain_info(repository, complete_domain_path, chatbot_info)
            print(chatbot_info)
            chatbot_info['responses_language'].append(get_language_from_domain(repository, complete_domain_path))
            print(chatbot_info)

    # NLU files
    r = re.compile(".*nlu.yml")
    nlu_list = list(filter(r.match, file_list))
    chatbot_info['nlu-files'] = nlu_list
    print(chatbot_info)

    # Language information
    for nlu_file in nlu_list:
        complete_domain_path = repo_info['full-name'].split('/')[1] + '-'+repo_info['default-branch']+'/' + nlu_file
        chatbot_info['training_phrases_language'].append(get_language_from_nlu(repository, nlu_file))
        print(chatbot_info)
    



def extract_domain_info(repository, file_path, chatbot_info):

    with repository.open(file_path) as domain_file:
        yaml_content = domain_file.read().decode()
        
        try:
            domain = yaml.safe_load(yaml_content)
            #print(domain)

            chatbot_info['intents'].append(domain['intents'])
            chatbot_info['n_intents'].append(len(domain['intents']))
            
            if 'entities' in domain:
                chatbot_info['entities'].append(domain['entities'])
                chatbot_info['n_entities'].append(len(domain['entities']))
            else:
                chatbot_info['entities'].append([])
                chatbot_info['n_entities'].append(0)
            
            if 'slots' in domain:
                slots = domain['slots']
                chatbot_info['slot_names'].append(list(slots.keys()))
                entity_types = []

                for entity in domain['entities']:
                    for slot_info in slots.values():
                        for mapping in slot_info['mappings']:
                            if mapping['type'] == 'from_entity' and mapping['entity'] == entity:
                                entity_types.append(slot_info['type'])
                                
                chatbot_info['slots_complete'].append(slots)
                chatbot_info['entity_types'].append(entity_types)
                chatbot_info['n_slots'].append(len(domain['slots']))
            else:
                chatbot_info['slots_complete'].append([])
                chatbot_info['n_slots'].append(0)

            if 'actions' in domain:
                chatbot_info['actions'].append(domain['actions'])
                chatbot_info['n_actions'].append(len(domain['actions']))
            else:
                chatbot_info['actions'].append([])
                chatbot_info['n_actions'].append(0)

            if 'version' in domain:
                chatbot_info['version'].append(domain['version'])
            else:
                chatbot_info['version'].append('unknown')
            
        except yaml.YAMLError as e:
            print(f"Parsing error for repository {repo_info['full-name']}: {e}")

    return chatbot_info
    

def get_language_from_domain(repository, file_path):
    with repository.open(file_path) as domain_file:
        yaml_content = domain_file.read().decode()
        
        try:
            domain = yaml.safe_load(yaml_content)
            
            default_responses = ['utter_iamabot', 'utter_greet', 'utter_goodbye']
            languages=[]
            responses = domain['responses']

            for default_response in default_responses:
                if len(responses) <= 2:
                    break

                if default_response in responses.keys():
                    print(f"Deleting response {default_response}\n\n\n")
                    del responses[default_response]

            phrases_sample = []
            random_key = random.choice(list(responses.keys()))
            #print(random_key)
            #print(responses[random_key])
            response_text = ""
            for response in responses[random_key]:
                 #print(response['text']+'\n\n')
                 response_text += re.sub(r'[\{].*?[\}]', '', response['text']).replace('\n-', ' ')
            phrases_sample.append(response_text)
            del responses[random_key]

            random_key = random.choice(list(responses.keys()))
            response_text = ""
            for response in responses[random_key]:

                response_text += re.sub(r'[\{].*?[\}]', '', response['text']).replace('\n-', ' ')

            phrases_sample.append(response_text)

            print(phrases_sample)

            
            language_response = [ [ {'isReliable': True, 'confidence': 12.04, 'language': 'es'} ],[ {'isReliable': True, 'confidence': 9.38, 'language': 'lt'} ] ]#detectlanguage.detect(phrases_sample)
            languages=[]
            languages.append(language_response[0][0]['language'])
            if language_response[1][0]['language'] != language_response[0][0]['language']:
                languages.append(language_response[1][0]['language'])
            
            return languages
        
        except yaml.YAMLError as e:
            print(f"Parsing error for repository {repo_info['full-name']}: {e}")
            



def get_language_from_nlu(repository, file_path):
    default_intents = ['bot_challenge', 'affirm', 'deny', 'greet', 'thankyou', 'goodbye', 'mood_great', 'mood_unhappy']

    with repository.open(file_path) as nlu_file:
        yaml_content = nlu_file.read().decode()
        try:
            nlu = yaml.safe_load(yaml_content)
            phrases_sample = []
            intents = nlu['nlu']

            for default_intent in default_intents:
                if len(intents) <= 2:
                    break

                for intent in intents:
                    if intent['intent'] == default_intent:
                        print(f"Deleting intent {intent['intent']}")
                        intents.remove(intent)

            language_intents = []
            language_intents.append(random.choice(intents))
            intents.remove(language_intents[0])
            language_intents.append(random.choice(intents))

            phrases_sample = []

            for language_intent in language_intents:
                clean_language_intent = language_intent['examples'].replace('\n-', ' ').replace('[', '').replace(']', '')
                clean_language_intent = re.sub(r'[\{\(].*?[\}\)]', '', clean_language_intent)
                phrases_sample.append(clean_language_intent)
            
            print(phrases_sample)

            language_response = [ [ {'isReliable': True, 'confidence': 12.04, 'language': 'es'} ],[ {'isReliable': True, 'confidence': 9.38, 'language': 'lt'} ] ]#detectlanguage.detect(phrases_sample)
            languages=[]
            languages.append(language_response[0][0]['language'])
            if language_response[1][0]['language'] != language_response[0][0]['language']:
                languages.append(language_response[1][0]['language'])
            
            return languages
            
        except yaml.YAMLError as e:
            print(f"Parsing error for repository {repo_info['full-name']}: {e}") 



repo = {}
repo['full-name'] = REPOSITORY


repo_file = open(CHATBOTS_FILE, 'r')
reader = csv.DictReader(repo_file, delimiter=CSV_SEPARATOR)
repos = list(reader)

repo_info = repos[300]
print(repo_info)
repo_info['domain-files'] = ast.literal_eval(repo_info['domain-files'])
print(repo_info)

def main(repository):
    
    #zip_path = download_zip(repository['full-name'], 'master')
    zip_path = "MainP0k_Bot_Rasa.zip"
    if zip_path != -1:
        analyze_repository(zip_path, repo_info)
        

main(repo)
