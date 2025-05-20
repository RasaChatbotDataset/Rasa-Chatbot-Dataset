import zipfile
import yaml
import ast
import csv
import os
import traceback


CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
RESULTS_FOLDER = 'results/09_results'
INPUT_FOLDER = 'results/08_results'

FIELDS = ['id', 'full-name','html-url','stars','forks', 'last-commit', 'domain-file', 'n-nlu-files', 'n-actions-files', 'n-language-files', 'n-readme-files',
    'n-intents', 'intents', 'n-entities', 'entities', 'n-actions', 'actions', 'n-actions-custom', 'actions-custom', 'n-slots', 'slots', 'n-slots-from-entity', 'n-slots-from-text', 
    'slots-type','n-forms', 'forms', 'version']

csv.field_size_limit(100000000)

# Initialize chatbot information
def initialize_chatbot_info(chatbot_info):
    for key in FIELDS[11:]:
        if key.startswith('n-'):
            chatbot_info[key] = 0
        else: 
            chatbot_info[key] = []
    return chatbot_info


# Extract domain information
def extract_domain_info(repository, file_path, chatbot_info):

    with repository.open(file_path) as domain_file:
        yaml_content = domain_file.read().decode()
        
        try:
            domain = yaml.safe_load(yaml_content)


            # Intents extraction
            if 'intents' in domain:
                intents = []
                if type(domain['intents']) == str:
                    chatbot_info['exception'] = 'Intents field is str, expected list'
                    return -1
                for intent in domain['intents']:
                    # Intent as a dictionary
                    if type(intent) == dict:
                        intents.append(list(intent.keys())[0])
                    # Intent as a string
                    else:
                        intents.append(intent)
                
                chatbot_info['intents'] = intents
                chatbot_info['n-intents'] = len(chatbot_info['intents'])


            # Entities extraction
            if 'entities' in domain:
                entities = []
                if type(domain['entities']) == str:
                    chatbot_info['exception'] = 'Entities field is str, expected list'
                    return -1
                for entity in domain['entities']:
                    # Entity as a dictionary
                    if type(entity) == dict:
                        entities.append(list(entity.keys())[0])
                    # Entity as a string
                    else:
                        entities.append(entity)

                chatbot_info['entities'] = entities
                chatbot_info['n-entities'] = len(chatbot_info['entities'])
    

            # Forms extraction
            if 'forms' in domain:
                forms = []
                if type(domain['forms']) == str:
                    chatbot_info['exception'] = 'Forms field is str, expected list'
                    return -1
                for form in domain['forms']:
                    # Form as a dictionary
                    if type(form) == dict:
                        forms.append(list(form.keys())[0])
                    # Form as a string
                    else:
                        forms.append(form)

                chatbot_info['forms'] = forms
                chatbot_info['n-forms'] = len(chatbot_info['forms'])

            
            # Slots extraction
            if 'slots' in domain:

                if type(domain['slots']) == str:
                    chatbot_info['exception'] = 'Slots field is str, expected list'
                    return -1

                chatbot_info['slots'] = []
                slot_types = []
                from_entity = 0
                from_text = 0

                slots = domain['slots']
                chatbot_info['slots'] = list(slots.keys())

                # Slots as a list
                if type(slots) == list:
                    chatbot_info['slots'] = slots
                # Slots as a dictionary  
                else:
                    chatbot_info['slots'] = list(slots.keys())

                    for slot_info in slots.values():
                        
                        # Slot type
                        if 'type' in slot_info:
                            slot_types.append(slot_info['type'])
                        # Slot mapping
                        if 'mappings' in slot_info:
                            for mapping in slot_info['mappings']:
                    
                                    if mapping['type'] == 'from_entity':
                                        from_entity += 1
                                    elif mapping['type'] == 'from_text':
                                        from_text += 1

                chatbot_info['n-slots-from-entity'] = from_entity
                chatbot_info['n-slots-from-text'] = from_text
                chatbot_info['slots-type'] = slot_types
                chatbot_info['n-slots'] = len(chatbot_info['slots'])

            # Actions extraction
            if 'actions' in domain:
                if type(domain['actions']) == str:
                    chatbot_info['exception'] = 'Action field is str, expected list'
                    return -1
                chatbot_info['actions']= domain['actions']
                chatbot_info['n-actions'] = len(domain['actions'])

            # Version extraction
            if 'version' in domain:
                chatbot_info['version'] = domain['version']
            else:
                chatbot_info['version'] = 'unknown'

             
        except Exception:
            print(f"Parsing error for repository {chatbot_info['full-name']}")
            chatbot_info['exception'] =  traceback.format_exc()
            return -1

    #print(chatbot_info)
    print('End domain extraction')
    return chatbot_info

def analyze_actions(chatbot_info, repository):
    chatbot_info['actions-custom'] = []

    for file in chatbot_info['actions-files']:

        full_path = chatbot_info['full-name'].split('/')[-1]+'-'+chatbot_info['last-commit']+ '/' + file
        action_file = repository.open(full_path)

        # Decode error
        try:
            content = action_file.read().decode()
        except:
            print(f"Decode error")
            continue

        for action in chatbot_info['actions']:
            if ('return\"'+str(action) in content.replace(' ', '') or 'return\''+str(action) in content.replace(' ', '') or str(action)=='action_query_knowledge_base') and action not in chatbot_info['actions-custom']:
                chatbot_info['actions-custom'].append(action)

    chatbot_info['n-actions-custom'] = len(chatbot_info['actions-custom'])
    return chatbot_info
    

CHATBOT_FILES = ['chatbot_repositories_sfsd', 'chatbot_repositories_sfmd', 'chatbot_repositories_mfsd', 'chatbot_repositories_mfmd']
ERROR_FILE = 'chatbot_repositories_errors.csv'

def main(): 

    # Result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Error file
    error_file = open(RESULTS_FOLDER + '/' +ERROR_FILE, 'w', newline='')
    error_writer = csv.DictWriter(error_file, delimiter=CSV_SEPARATOR, fieldnames=FIELDS[:10] + ['chatbot-type', 'exception'], extrasaction='ignore')
    error_writer.writeheader()

    for file in CHATBOT_FILES:

        # Open files
        chatbot_file = open(INPUT_FOLDER + '/' +file+'.csv', 'r')
        reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
        chatbots = list(reader)

        analysis_file = open(RESULTS_FOLDER + '/' +file+'_info.csv', 'w', newline='')
        analysis_writer = csv.DictWriter(analysis_file, delimiter=CSV_SEPARATOR, fieldnames=FIELDS, extrasaction='ignore')
        analysis_writer.writeheader()

        for chatbot_info in chatbots:
            print(chatbot_info['full-name'])
            chatbot_info['domain-files'] = ast.literal_eval(chatbot_info['domain-files'])
            chatbot_info['actions-files'] = ast.literal_eval(chatbot_info['actions-files'])

            # Open zip archive
            zip_path = ZIP_FOLDER + '/' + chatbot_info['full-name'].replace('/', '_') + '.zip'
            repository =  zipfile.ZipFile(zip_path, 'r')
            file_list = repository.namelist()  

            for domain in chatbot_info['domain-files']:

                chatbot_info = initialize_chatbot_info(chatbot_info)
                chatbot_info['domain-file'] = domain
    
                # Domain information
                complete_domain_path = chatbot_info['full-name'].split('/')[1] + '-'+chatbot_info['last-commit']+'/' + domain
                if complete_domain_path in file_list:
                    print(f"Analyzing domain file {complete_domain_path}")
                    result = extract_domain_info(repository, complete_domain_path, chatbot_info)
                    if result == -1:
                        chatbot_info['chatbot-type'] = file.replace('chatbot_repositories_', '').replace('.csv', '')
                        error_writer.writerow(chatbot_info)
                    else:
                        if int(result['n-actions-files']) != 0 and int(result['n-actions'] != 0):
                            result=analyze_actions(result, repository)
                        else:
                            result['actions-custom'] = []
                            result['n-actions-custom'] = 0
                        analysis_writer.writerow(result)

                else:
                    quit()

        # Close files
        analysis_file.close()
        chatbot_file.close()
    error_file.close()

main()
