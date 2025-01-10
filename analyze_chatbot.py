import requests
import zipfile
import yaml
import ast
import detectlanguage
import csv
from dotenv import dotenv_values
import re
import random
#from openai import AzureOpenAI
import os
import copy
import git
import shutil
import stat

config = dotenv_values('config.env')

KEYWORDS  = ['intents']

CHATBOTS_FILE_NAME = 'chatbots.csv'
CSV_SEPARATOR= ';'
ANALYSIS_FILE_NAME = 'chatbot_dataset.csv'
CHATGPT_RESPONSE_FOLDER = 'chatgpt_responses'

EXTRACT_FIELDS = [
    'n-entities', 'total-entities', 'max-entities', 'n-actions', 'total-actions', 'max-actions', 'n-intents', 'total-intents', 'max-intents',
    'n-slots', 'total-slots', 'max-slots', 'entities', 'actions','intents', 'slots-complete', 'slot-names', 'mapped-entities', 'entity-types',
    'version', 'training-phrases-language', 'responses-language', 'english', 'external-services-usage', 
    'external-services', 'external-services-response', 'nlu-files', 'actions-files'
]

detectlanguage.configuration.api_key = config['DETECT_LANGUAGE_KEY']
  
# Download GitHub repository
def download_zip(repo_name, branch):
    download_url = f"https://github.com/{repo_name}/archive/refs/heads/{branch}.zip"
    print(download_url)
    
    try: 
        response = requests.get(download_url, timeout=300)
        if response.status_code != 200:
            print(f'Error in repository {repo_name} ZIP download: {response.status_code}')
            return -1
        else:
            zip_path = f"{repo_name.replace('/', '_')}.zip"
            with open(zip_path, "wb") as f:
                f.write(response.content)
            return zip_path
    except requests.exceptions.Timeout:
        print(f"Timeout in repository {repo_name} ZIP download")
        return 0
    

# Clone and compress GitHub repository
def clone_and_compress_repo(repo):

    clone_dir = 'temp_dir'
    if not os.path.exists(clone_dir):
        os.makedirs(clone_dir)
    
    try:
        print(f"Cloning repository {repo['html-url']}...")
        git.Repo.clone_from(repo['html-url'], clone_dir)
    except git.exc.GitCommandError as e:
        print(f"Error cloning repository: {repo['html-url']} {e}")
        return
    print('Cloned')
    gitignore_path = os.path.join(clone_dir, '.gitignore')
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w') as f:
            f.write("# Ignore .tar.gz\n")
            f.write("*.tar.gz\n")
    else:
        with open(gitignore_path, 'a') as f:
            f.write("# Ignore .tar.gz\n")
            f.write("*.tar.gz\n")
    
    # Zip compression
    zip_name = repo['full-name'].replace('/', '_')
    shutil.make_archive(zip_name, 'zip', clone_dir)

    shutil.rmtree(clone_dir, onexc = redo_with_write)
    return zip_name+'.zip'

def redo_with_write(redo_func, path, err):
    os.chmod(path, stat.S_IWRITE)
    redo_func(path)

# Initialize chatbot information
def initialize_chatbot_info(chatbot_info):
    for key in EXTRACT_FIELDS:
        if key.startswith('max') or key.startswith('total'):
            chatbot_info[key] = 0
        elif key == 'english':
            chatbot_info[key] = 'unknown'
        else: 
            chatbot_info[key] = []
    return chatbot_info

# Analyze chatbot repository
def analyze_repository(zip_path, repo_info):

    # Chatbot info initialization
    chatbot_info = copy.deepcopy(repo_info)
    chatbot_info = initialize_chatbot_info(chatbot_info)
    chatbot_info['domain-files'] = ast.literal_eval(chatbot_info['domain-files'])
    print(chatbot_info['domain-files'])
    
    repository =  zipfile.ZipFile(zip_path, 'r')
    file_list = repository.namelist()

    # Domain information
    for domain_file_path in chatbot_info['domain-files']:
        complete_domain_path = chatbot_info['full-name'].split('/')[1] + '-'+chatbot_info['default-branch']+'/' + domain_file_path
        print(f"domain file {complete_domain_path}")
        if complete_domain_path in file_list:
            print(f"Analyzing domain file {complete_domain_path}")
            chatbot_info = extract_domain_info(repository, complete_domain_path, chatbot_info, domain_file_path)
            print(chatbot_info)

            # Response language information
            if domain_file_path in chatbot_info['domain-files']:
                chatbot_info['responses-language'].append(get_language_from_domain(repository, complete_domain_path))
                print(chatbot_info)
        else:
            quit()

    # Sum and max domain information
    chatbot_info['total-entities'] = sum(chatbot_info['n-entities'])
    chatbot_info['max-entities'] = max(chatbot_info['n-entities'])
    chatbot_info['total-actions'] = sum(chatbot_info['n-actions'])
    chatbot_info['max-actions'] = max(chatbot_info['n-actions'])
    chatbot_info['total-intents'] = sum(chatbot_info['n-intents'])
    chatbot_info['max-intents'] = max(chatbot_info['n-intents'])
    chatbot_info['total-slots'] = sum(chatbot_info['n-slots'])
    chatbot_info['max-slots'] = max(chatbot_info['n-slots'])


    # NLU files
    r = re.compile(".*nlu.*.yml")
    nlu_list = list(filter(r.match, file_list))
    chatbot_info['nlu-files'] = nlu_list
    print(chatbot_info)

    # Training language information
    for nlu_file in nlu_list:
       # complete_domain_path = chatbot_info['full-name'].split('/')[1] + '-'+chatbot_info['default-branch']+'/' + nlu_file
        chatbot_info['training-phrases-language'].append(get_language_from_nlu(repository, nlu_file))
        print(chatbot_info)
    
    # English check
    training_english = False
    for languages in chatbot_info['training-phrases-language']:
        if 'en' in languages:
            training_english = True
    
    responses_english = False
    for languages in chatbot_info['responses-language']:
        if 'en' in languages:
            responses_english = True
    
    if responses_english and training_english:
        chatbot_info['english'] = True
    else:
        chatbot_info['english'] = False
    

    
    # External services
    r = re.compile(".*actions.py")
    actions_file_list = list(filter(r.match, file_list))
    chatbot_info['actions-files'] = actions_file_list
    for action_file in actions_file_list:
        chatbot_info = get_external_services(repository, action_file, chatbot_info)

    return chatbot_info

# Query OpenAI ChatGPT
def query_chatgpt(prompt):

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
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 800
    }
    ENDPOINT = config['OPENAI_ENDPOINT']
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()

    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")
    
    return response.json()


# Extract external services with ChatGPT
def get_external_services(repository, action_file_path, chatbot_info):

    with repository.open(action_file_path) as action_file:
        action_script = action_file.read().decode()
        prompt = f"Does this rasa chatbot actions.py file use any database (local or external) or any external service?\
                Begins the answer with YES if it does or NO if it doesn't, a list of these databases and services (only names on a single line, no further explanation, no numeration)\
                and in a new section titled \"Purpose of external services\" explain the purpose of each service. {action_script}"
        response = query_chatgpt(prompt)
        content = response['choices'][0]['message']['content']
        response_file_name = CHATGPT_RESPONSE_FOLDER+'/'+chatbot_info['full-name'].replace('/', '_')+'.txt'
        response_file = open(response_file_name, 'w')
        response_file.write(content)
        response_file.close()
        chatbot_info['external-services-response'].append(response_file_name)

        print(content)
        if content.startswith('YES'):
            content = content.replace('YES', '', 1)
            chatbot_info['external-services-usage'].append('YES')

            external_services = re.split('Purpose of External Services', content, flags=re.IGNORECASE)[0].strip('\n').replace('\n', ',').strip().strip(':')
            chatbot_info['external-services'].append(external_services)
            print(external_services)

        elif content.startswith('NO'):
            content.replace('NO', '', 1)
            chatbot_info['external-services-usage'].append('NO')
        
    return chatbot_info

        
# Extract domain information
def extract_domain_info(repository, file_path, chatbot_info, domain_file_path):
    print('Extracting info')

    with repository.open(file_path) as domain_file:
        yaml_content = domain_file.read().decode()
        
        try:
            domain = yaml.safe_load(yaml_content)
            #print(domain)

            if 'intents' in domain:
                chatbot_info['intents'].append(domain['intents'])
                chatbot_info['n-intents'].append(len(domain['intents']))
            else:
                chatbot_info['domain-files'].remove(domain_file_path)
                return chatbot_info
            
            if 'entities' in domain:
                chatbot_info['entities'].append(domain['entities'])
                chatbot_info['n-entities'].append(len(domain['entities']))
            else:
                chatbot_info['entities'].append([])
                chatbot_info['n-entities'].append(0)
            
            if 'slots' in domain:
                slots = domain['slots']
                chatbot_info['slot-names'].append(list(slots.keys()))
                entity_types = []
                mapped_entities = []

                for entity in domain['entities']:
                    for slot_info in slots.values():
                        if 'mappings' in slot_info:
                            for mapping in slot_info['mappings']:
                                if mapping['type'] == 'from_entity' and mapping['entity'] == entity:
                                    entity_types.append(slot_info['type'])
                                    mapped_entities.append(entity)

                                
                chatbot_info['slots-complete'].append(slots)
                chatbot_info['entity-types'].append(entity_types)
                chatbot_info['mapped-entities'].append(mapped_entities)
                chatbot_info['n-slots'].append(len(domain['slots']))
            else:
                chatbot_info['slots-complete'].append([])
                chatbot_info['n-slots'].append(0)

            if 'actions' in domain:
                chatbot_info['actions'].append(domain['actions'])
                chatbot_info['n-actions'].append(len(domain['actions']))
            else:
                chatbot_info['actions'].append([])
                chatbot_info['n-actions'].append(0)

            if 'version' in domain:
                chatbot_info['version'].append(domain['version'])
            else:
                chatbot_info['version'].append('unknown')
            
        except yaml.YAMLError as e:
            print(f"Parsing error for repository {chatbot_info['full-name']}: {e}")

    print(chatbot_info)
    print('End domain extraction')
    return chatbot_info
    

# Extract response language from domain file
def get_language_from_domain(repository, file_path):
    with repository.open(file_path) as domain_file:
        yaml_content = domain_file.read().decode()
        
        try:
            domain = yaml.safe_load(yaml_content)
            
            default_responses = ['utter_iamabot', 'utter_greet', 'utter_goodbye']
            languages=[]

            if 'responses' not in domain:
                return languages
            
            responses = domain['responses']

            for default_response in default_responses:
                if len(responses) <= 2:
                    break

                if default_response in responses.keys():
                    print(f"Deleting response {default_response}\n\n\n")
                    del responses[default_response]

            phrases_sample = []
            random_key = random.choice(list(responses.keys()))

            response_text = ""
            for response in responses[random_key]:
                
                response_text += re.sub(r'[\{].*?[\}]', '', response['text']).replace('\n-', ' ')
            phrases_sample.append(response_text)
            del responses[random_key]

            random_key = random.choice(list(responses.keys()))
            response_text = ""
            for response in responses[random_key]:

                response_text += re.sub(r'[\{].*?[\}]', '', response['text']).replace('\n-', ' ')

            phrases_sample.append(response_text)

            language_response = detectlanguage.detect(phrases_sample)#[ [ {'isReliable': True, 'confidence': 12.04, 'language': 'es'} ],[ {'isReliable': True, 'confidence': 9.38, 'language': 'lt'} ] ]#
            languages=[]
            languages.append(language_response[0][0]['language'])
            if language_response[1][0]['language'] != language_response[0][0]['language']:
                languages.append(language_response[1][0]['language'])
            
            return languages
        
        except yaml.YAMLError as e:
            print(f"Parsing error for file {file_path}: {e}")
            


# Extract training phrases language from nlu file
def get_language_from_nlu(repository, file_path):
    default_intents = ['bot_challenge', 'affirm', 'deny', 'greet', 'thankyou', 'goodbye', 'mood_great', 'mood_unhappy']

    with repository.open(file_path) as nlu_file:
        yaml_content = nlu_file.read().decode()
        try:
            nlu = yaml.safe_load(yaml_content)
            phrases_sample = []
            languages=[]

            if 'nlu' not in nlu:
                return languages
            
            intents = nlu['nlu']

            intents = [d for d in intents if 'intent' in d]
            print(intents)

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
            
            #print(phrases_sample)

            language_response = detectlanguage.detect(phrases_sample)#[ [ {'isReliable': True, 'confidence': 12.04, 'language': 'es'} ],[ {'isReliable': True, 'confidence': 9.38, 'language': 'lt'} ] ]#detectlanguage.detect(phrases_sample)
            
            languages.append(language_response[0][0]['language'])
            if language_response[1][0]['language'] != language_response[0][0]['language']:
                languages.append(language_response[1][0]['language'])
            
            return languages
            
        except yaml.YAMLError as e:
            print(f"Parsing error for file {nlu_file}: {e}") 
            return []



def main(): 
    chatbot_file = open(CHATBOTS_FILE_NAME, 'r')
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    if not os.path.exists(CHATGPT_RESPONSE_FOLDER):
        os.makedirs(CHATGPT_RESPONSE_FOLDER)

    analysis_file = open(ANALYSIS_FILE_NAME, 'w', newline='')
    header = reader.fieldnames + EXTRACT_FIELDS
    analysis_writer = csv.DictWriter(analysis_file, delimiter=CSV_SEPARATOR, fieldnames=header)
    analysis_writer.writeheader()

    for chatbot in chatbots[300:301]:
        print(chatbot['full-name'])
        # Download repository
        zip_path = download_zip(chatbot['full-name'], chatbot['default-branch'])# clone_and_compress_repo(chatbot)
        print('Download completed')
        zip_path = 'MainP0k_Bot_Rasa.zip'
        if zip_path != -1:
            # Analyze repository
            chatbot_info = analyze_repository(zip_path, chatbot)
            print(chatbot_info)
            # Save on file
            analysis_writer.writerow(chatbot_info)
        else:
            print(f"Error in downloading repository {chatbot['full-name']}")

    analysis_file.close()

main()
