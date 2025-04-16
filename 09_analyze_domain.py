import zipfile
import yaml
import ast
import csv
import os


CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
RESULTS_FOLDER = 'results/09_results'
INPUT_FOLDER = 'results/08_results'

FIELDS = ['id', 'full-name','html-url','stars','forks', 'last-commit', 'domain-file', 'n-nlu-files', 'n-actions-files', 'n-language-files', 'n-readme-files',
    'n-intents', 'intents', 'n-entities', 'entities', 'n-actions', 'actions', 'n-slots', 'slots', 'n-slots-from-entity', 'n-slots-from-text', 
    'slots-type','n-forms', 'forms', 'version'
]

  

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

                chatbot_info['slots'] = []
                slot_types = []
                from_entity = 0
                from_text = 0

                slots = domain['slots']
                chatbot_info['slots'] = list(slots.keys())

                if type(slots) == list:
                    chatbot_info['slots'] = slots
                    
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
                chatbot_info['actions']= domain['actions']
                chatbot_info['n-actions'] = len(domain['actions'])

            # Version extraction
            if 'version' in domain:
                chatbot_info['version'] = domain['version']
            else:
                chatbot_info['version'] = 'unknown'

             
        except Exception as e:
            print(f"Parsing error for repository {chatbot_info['full-name']}")
            chatbot_info['exception'] = e
            return -1

    #print(chatbot_info)
    print('End domain extraction')
    return chatbot_info
    

CHATBOT_FILES = ['chatbot_repositories_sfsd', 'chatbot_repositories_sfmd', 'chatbot_repositories_mfsd', 'chatbot_repositories_mfmd']
ERROR_FILE = 'chatbot_repositories_errors.csv'

def main(): 

    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    error_file = open(RESULTS_FOLDER + '/' +ERROR_FILE, 'w', newline='')
    error_writer = csv.DictWriter(error_file, delimiter=CSV_SEPARATOR, fieldnames=FIELDS[:10] + ['chatbot-type', 'exception'], extrasaction='ignore')
    error_writer.writeheader()

    for file in CHATBOT_FILES:

        chatbot_file = open(INPUT_FOLDER + '/' +file+'.csv', 'r')
        reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
        chatbots = list(reader)

        analysis_file = open(RESULTS_FOLDER + '/' +file+'_info.csv', 'w', newline='')
        analysis_writer = csv.DictWriter(analysis_file, delimiter=CSV_SEPARATOR, fieldnames=FIELDS, extrasaction='ignore')
        analysis_writer.writeheader()

        for chatbot_info in chatbots:
            print(chatbot_info['full-name'])
            chatbot_info['domain-files'] = ast.literal_eval(chatbot_info['domain-files'])

 
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
                        analysis_writer.writerow(result)

                else:
                    quit()


        analysis_file.close()
        chatbot_file.close()
    error_file.close()

main()
