import detectlanguage
import yaml
import json
import zipfile
import ast
import os
import pandas as pd
import re
from dotenv import dotenv_values
import random

config = dotenv_values('config.env')
detectlanguage.configuration.api_key = config['DETECT_LANGUAGE_KEY']


FILES = ['results/08_results/chatbot_repositories_sfsd.csv', 'results/08_results/chatbot_repositories_mfsd.csv', 'results/08_results/chatbot_repositories_sfmd.csv', 'results/08_results/chatbot_repositories_mfmd.csv']
RESULTS_FOLDER = 'results/13_results/'
CHATBOT_FILE = 'results/12_results/chatbots.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'


# Extract language from configuration file
def extract_training_language(chatbot):

    # Get all configuration file from repository
    zip_path = ZIP_FOLDER + '/' + chatbot['full-name'].replace('/', '_') + '.zip'
    repository =  zipfile.ZipFile(zip_path, 'r')

    file_list = ast.literal_eval(chatbot['nlu-files'])
    languages = []
    version = chatbot['version']

    for file in file_list:
        # Extract version and training language
        nlu_version, file_languages = extract_training_language_from_file(chatbot, file, repository)

        if nlu_version == -1:
            continue

        # Version check
        if version == 'unknown' and nlu_version != 'unknown':
            version = nlu_version

        # Update languages
        for l in file_languages:
            if l not in languages:
                languages.append(l)

    return version, languages



# Extract training language from single file
def extract_training_language_from_file(chatbot, file, repository):

    languages = []
    version = None
    default_intents = ['bot_challenge', 'affirm', 'deny', 'greet', 'thankyou', 'goodbye', 'mood_great', 'mood_unhappy']
    full_config_path = chatbot['full-name'].split('/')[-1]+'-'+chatbot['last-commit']+ '/' + file

    # Open file
    with repository.open(full_config_path) as nlu_file:
        try:
            # Decode file
            content = nlu_file.read().decode()

            # YML file
            if file.endswith('.yml'):
                content = yaml.safe_load(content)

                # Check for version
                if 'version' in content:
                    version = content['version']
                try:
                    if 'nlu' in content and len(content['nlu']) != 0:
                        intents = content['nlu']
                    else:
                        return -1, -1
                except:
                    print('Incomplete nlu object')
                    return -1, -1
                
                # Keep only intents
                intents = [d for d in intents if 'intent' in d]
                if len(intents) == 0:
                    return -1, -1
                
                # Remove incomplete intents
                try:
                    for intent in intents[:]:
                        if 'examples' not in intent:
                            intents.remove(intent)
                        elif not isinstance(intent['examples'], str):
                            if 'text' in intent['examples']:
                                texts = [example['text'] for example in intent['examples']]
                                intent['examples'] = ' '.join(texts)
                            else:
                                intent['examples'] = ' '.join(intent['examples'])
                except Exception as e:
                    print(f'Exception {e} for file {file}')
                    return -1, -1
                
                if not intents:
                    return -1, -1

                # Remove default intents 
                for default_intent in default_intents:
                    if len(intents) <= 2:
                        break
                    for intent in intents[:]:
                        if intent['intent'] == default_intent:
                            intents.remove(intent)
                
                # Random selection of 2 intents in nlu file
                language_intents = []
                language_intents.append(random.choice(intents))
                if len(intents) > 1:
                    intents.remove(language_intents[0])
                language_intents.append(random.choice(intents))
                
                # Intent training phrases selection and cleaning
                phrases_sample = []
                for language_intent in language_intents:
                    clean_language_intent = language_intent['examples'].replace('\n-', ' ').replace('[', '').replace(']', '')
                    clean_language_intent = re.sub(r'[\{\(].*?[\}\)]', '', clean_language_intent)
                    phrases_sample.append(clean_language_intent)

            else:
                # JSON files
                if file.endswith('.json'):
                    intents = parse_json(content)
                    if intents == -1:
                        return -1, -1
                # Markdown files
                else:
                    intents = parse_md(content)

                if not intents:
                    return -1, -1

                # Remove default intents
                for default_intent in default_intents:
                    if len(intents) <= 2:
                        break

                    for intent in list(intents.keys()):
                        if intent == default_intent:
                            del intents[intent]
                
                # Random selection of 2 intents in nlu file
                phrases_sample = []
                language_intent = random.choice(list(intents.keys()))
                phrases_sample.append(intents[language_intent])
                if len(intents) > 1:
                    del intents[language_intent]
                    phrases_sample.append(intents[random.choice(list(intents.keys()))])
            
            # Detect language of sample training phrases
            response = detectlanguage.detect(phrases_sample)#[ [ {'isReliable': True, 'confidence': 12.04, 'language': 'es'} ],[ {'isReliable': True, 'confidence': 9.38, 'language': 'lt'} ] ]
            
            for lang in response:
                if lang and lang[0]['language'] not in languages:
                    languages.append(lang[0]['language'])

        except UnicodeDecodeError as e:
            print(f"Decode error")
        except yaml.YAMLError as e:
            print("Yaml parsing error")
    

    return version, languages



# Parse json nlu into python dictionary intent-phrases
def parse_json(json_content):
    content = json.loads(json_content)
    if 'common_examples' not in content['rasa_nlu_data']:
        return -1
    
    intent_phrases = content['rasa_nlu_data']['common_examples']
    intents = {}

    # Dictionary with intent name as key and sequence of phrases as value
    for phrase in intent_phrases:
        if 'intent' in phrase:
            if phrase['intent'] not in intents:
                intents[phrase['intent']] = phrase['text']
            else:
                intents[phrase['intent']] = intents[phrase['intent']] + ' ' + phrase['text']
    
    return intents



# Parse md nlt into python dictionary intent-phrases
def parse_md(md_content):

    intents = {}
    lines = md_content.strip().split('\n')
    
    current_intent = None
    phrases = []
    no_intent = False

    for line in lines:
        # New intent
        if line.startswith('## intent'):
            
            # Previuos intent ended
            if current_intent:
                intents[current_intent] = ' '.join(phrases)
            
            # New current intent
            current_intent = line.replace('## intent:', '').strip()
            phrases = [] 
            no_intent = False
        
        # Sentence of current intent
        elif line.startswith("-") and not no_intent:
            # Cleaning
            line = re.sub(r'[\{\(].*?[\}\)]', '', line)
            line = line.replace('[', '').replace(']', '').strip('-').strip()
            phrases.append(line)
        
        # Synonym or other fields
        elif line.startswith('## '):
            no_intent = True


    # Last intent
    if current_intent:
        intents[current_intent] = ' '.join(phrases)
    
    return intents

           

def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Join chatbot files
    chatbots = pd.read_csv(CHATBOT_FILE, sep=CSV_SEPARATOR)
    cb_files = pd.DataFrame()

    # Merge with nlu files
    for file in FILES:
        cb_with_files = pd.read_csv(file, sep=CSV_SEPARATOR)
        cb_with_files = cb_with_files[['id', 'nlu-files']]
        cb_files = pd.concat([cb_files, cb_with_files])

    chatbots = pd.merge(chatbots, cb_files, how='inner')

    chatbots.to_csv(RESULTS_FOLDER + 'chatbots_join_nlu_file.csv', sep=CSV_SEPARATOR, index=False)
    chatbots['training-language'] = None
    
    for index, chatbot in chatbots.iterrows():

        if chatbot['n-nlu-files'] > 0 :
            print(chatbot['full-name'])
            
            # Check API limit
            language_api_status = detectlanguage.user_status()
            if language_api_status['requests'] == language_api_status['daily_requests_limit'] or language_api_status['bytes'] > language_api_status['daily_bytes_limit'] - 10000:
                print('Detect language API daily limit exceeded')
                break

            # Extract training language
            version, traning_language = extract_training_language(chatbot)
            chatbots.at[index, 'training-language'] = traning_language
            chatbots.at[index, 'version'] = version
        
        if chatbot['version'] == 'unknown':
            chatbot['version'] = None

    # Remove columns
    chatbots = chatbots.drop('n-nlu-files', axis=1)
    chatbots = chatbots.drop('nlu-files', axis=1)

    # Write dataset
    chatbots.to_csv(RESULTS_FOLDER + 'chatbots.csv', sep=CSV_SEPARATOR, index=False)



main()