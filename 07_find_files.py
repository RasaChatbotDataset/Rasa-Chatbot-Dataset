import zipfile
import ast
import csv
import re
import yaml
import json
from pathlib import Path
import os

RESULTS_FOLDER = 'results/07_results'
CHATBOTS_FILE_NAME = 'results/06_results/chatbot_repositories.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
CHATBOTS_ANALYSIS_FILE_NAME = RESULTS_FOLDER + '/' +'chatbot_repositories_files.csv'

# Find nlu files
def find_nlu_files(repository, chatbot_info, domain_is_test, domain_is_model): 

    file_list = repository.namelist()

    # NLU files information
    chatbot_info['nlu-files'] = []
    chatbot_info['n-nlu-yml'] = 0
    chatbot_info['n-nlu-md'] = 0
    chatbot_info['n-nlu-json'] = 0
    chatbot_info['n-nlu-files'] = 0
    chatbot_info['nlu-folders'] = []
    chatbot_info['n-nlu-folders'] = 0

    test_md = []

    for file in file_list:

        # Discard file with extension other than yml, json and md
        if not (file.endswith('.yml') or file.endswith('.md') or file.endswith('.json')):
            continue

        # Discard programming languages libraries
        if 'node_modules' in file or 'site-packages' in file or 'vendor/' in file or 'assets/libs' in file:
            continue


        clean_file_name = file.split(chatbot_info['last-commit']+'/')[-1]
        nlu_file = repository.open(file) 

        # Decode error
        try:
            content = nlu_file.read().decode()
        except:
            print(f"Decode error")
            continue

        # YML files
        if file.endswith('.yml'):
            
            # Discard other yml files
            if 'docker-compose.yml' in file or 'stories.yml' in file or 'rules.yml' in file:
                continue

            # Discard domain files
            is_domain = False
            for domain in chatbot_info['domain-files']:
                if clean_file_name == domain:
                    is_domain = True

            if is_domain:
                continue

            try:
                yml_content = yaml.safe_load(content)
                # NLU file
                if 'nlu' in yml_content:
                    if 'test' in clean_file_name and not domain_is_test:
                        test_md.append(clean_file_name)
                    elif 'models' in clean_file_name and not domain_is_model:
                         test_md.append(clean_file_name)
                    else:
                        chatbot_info['nlu-files'].append(clean_file_name)
                        chatbot_info['n-nlu-yml'] += 1

            except Exception as e:
                print('YML parsing error')

        # JSON files       
        elif file.endswith('.json'):
            try:
                json_content = json.loads(content)
                # NLU file
                if 'rasa_nlu_data' in json_content:
                    if 'test' in clean_file_name and not domain_is_test:
                        test_md.append(clean_file_name)
                    elif 'models' in clean_file_name and not domain_is_model:
                         test_md.append(clean_file_name)
                    else:
                        chatbot_info['nlu-files'].append(clean_file_name)
                        chatbot_info['n-nlu-json'] +=1
            except:
                print('JSON parsing error')
        
        elif file.endswith('.md') and file.split('/')[-1] != 'README.md' and file.split('/')[-1] != 'readme.md':
            # NLU file
            if '## intent:' in content:
                if 'test' in clean_file_name and not domain_is_test:
                    test_md.append(clean_file_name)
                elif 'models' in clean_file_name and not domain_is_model:
                    test_md.append(clean_file_name)
                else:
                    chatbot_info['nlu-files'].append(clean_file_name)
                    chatbot_info['n-nlu-md'] +=1
        
    if len(chatbot_info['nlu-files']) == 0 and len(test_md) != 0:
            chatbot_info['nlu-files'] = test_md
    
    chatbot_info['n-nlu-files'] = len(chatbot_info['nlu-files'])

    # Append nlu folder
    for nlu_name in chatbot_info['nlu-files']:
        if str(Path(nlu_name).parent) not in chatbot_info['nlu-folders']:
            chatbot_info['nlu-folders'].append(str(Path(nlu_name).parent))  

    chatbot_info['n-nlu-folders'] = len(chatbot_info['nlu-folders']) 

    return chatbot_info


# Find action files
def find_action_files(repository, chatbot_info, domain_is_test, domain_is_model):

    test_md = []

    file_list = repository.namelist()

    # Select python files named actions.py or in folder actions
    file_regex = re.compile(".*actions.*\\.py$")
    folder_regex = re.compile(".*actions.*/.*\\.py$")

    actions_file_list = list(filter(file_regex.match, file_list))
    actions_file_list += list(filter(folder_regex.match, file_list))
    actions_file_list = set(actions_file_list)

    chatbot_info['actions-files'] = []
    chatbot_info['actions-folders'] = []
    chatbot_info['n-actions-files'] = 0
    chatbot_info['n-actions-folders'] = 0

    for file in actions_file_list:

        # Discard python libraries / python packages files
        if 'site-packages' in file or file.endswith('__init__.py'):
            continue

        action_file = repository.open(file)

        # Decode error
        try:
            content = action_file.read().decode()
        except:
            print(f"Decode error")
            continue

        # Discard empty files         
        if len(content) == 0:
            continue

        # Discard completely commented files  
        all_comment = True

        for line in content.split('\n'):
            if not line.startswith('#') and not line == '' and not line.strip() == '':
                all_comment = False
        
        if all_comment:
            continue

        clean_file_name = file.split(chatbot_info['last-commit']+'/')[-1]

        if 'test' in clean_file_name and not domain_is_test:
            test_md.append(clean_file_name)
        elif 'models' in clean_file_name and not domain_is_model:
            test_md.append(clean_file_name)
        else:
            chatbot_info['actions-files'].append(clean_file_name)
        
    
    if len(chatbot_info['actions-files']) == 0 and len(test_md) != 0:
            chatbot_info['actions-files'] = test_md
    
    chatbot_info['n-actions-files'] = len(chatbot_info['actions-files'])

    for actions_name in chatbot_info['actions-files']:
        if str(Path(actions_name).parent) not in chatbot_info['actions-folders']:
            chatbot_info['actions-folders'].append(str(Path(actions_name).parent))
                                    
    chatbot_info['n-actions-folders'] = len(chatbot_info['actions-folders'])

    return chatbot_info


def find_readme_files(repository, chatbot_info, domain_is_test, domain_is_model):
    test_md = []

    chatbot_info['readme-files'] = []
    chatbot_info['n-readme-files'] = 0
    chatbot_info['readme-folders'] = []
    chatbot_info['n-readme-folders'] = 0

    file_list = repository.namelist()
    readme_regex = re.compile(".*README\\.md$")
    readme_file_list = list(filter(readme_regex.match, file_list))

    for readme in readme_file_list:
        clean_file_name = readme.split(chatbot_info['last-commit']+'/')[-1]

        # Discard programming languages libraries
        if 'node_modules' in readme or 'site-packages' in readme or 'vendor/' in readme or 'assets/libs' in readme:
            continue

        if 'test' in clean_file_name and not domain_is_test:
            test_md.append(clean_file_name)
        elif 'models' in clean_file_name and not domain_is_model:
            test_md.append(clean_file_name)
        else:
            chatbot_info['readme-files'].append(clean_file_name)


    if len(chatbot_info['readme-files']) == 0 and len(test_md) != 0:
            chatbot_info['readme-files'] = test_md   

    chatbot_info['n-readme-files'] = len(chatbot_info['readme-files'])

    for readme_name in chatbot_info['readme-files']:
        if str(Path(readme_name).parent) not in chatbot_info['readme-folders']:
            chatbot_info['readme-folders'].append(str(Path(readme_name).parent))
                                    
    chatbot_info['n-readme-folders'] = len(chatbot_info['readme-folders'])


    return chatbot_info



def find_language_files(repository, chatbot_info, domain_is_test, domain_is_model): 
        
    test_md = []

    file_list = repository.namelist()

    # Training language information
    chatbot_info['language-files'] = []
    chatbot_info['n-language-files'] = 0
    chatbot_info['language-folders'] = []
    chatbot_info['n-language-folders'] = 0

    for file in file_list:

        clean_file_name = file.split(chatbot_info['last-commit']+'/')[-1]
        
        # Discard not .yml and .json files
        if not file.endswith('.yml') and not file.endswith('.json'):
            continue
        
        # Discard files that are not configuration files
        if file.endswith('docker-compose.yml'):
            continue
        
        # Discard programming languages libraries
        if 'node_modules' in file or 'site-packages' in file or 'vendor/' in file or 'assets/libs' in file:
            continue

        language_file = repository.open(file)

        # Decode error
        try:
            content = language_file.read().decode()
        except:
            print(f"Decode error")
            continue
        
        # YML files
        if file.endswith('.yml'):
            try:      
                file_content = yaml.safe_load(content)
            except:
                print(f"YML parsing error")
                continue

        # JSON files
        elif file.endswith('.json'):
            try:
                file_content = json.loads(content)
            except:
                print(f"JSON parsing error")
                continue
        
        try:
            if len(file_content) == 0:
                continue
        except:
            print('Language file content error')
            continue
        
        if 'language' in file_content:
            if 'test' in clean_file_name and not domain_is_test:
                test_md.append(clean_file_name)
            elif 'models' in clean_file_name and not domain_is_model:
                test_md.append(clean_file_name)
            else:
                chatbot_info['language-files'].append(clean_file_name)
    
    if len(chatbot_info['language-files']) == 0 and len(test_md) != 0:
        chatbot_info['language-files'] = test_md
    
    chatbot_info['n-language-files'] = len(chatbot_info['language-files'])

    for lang_name in chatbot_info['language-files']:
        if str(Path(lang_name).parent) not in chatbot_info['language-folders']:
            chatbot_info['language-folders'].append(str(Path(lang_name).parent))
                                    
    chatbot_info['n-language-folders'] = len(chatbot_info['language-folders'])

    return chatbot_info




def main():

    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    chatbot_file = open(CHATBOTS_FILE_NAME, 'r')
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    multi_file = open(CHATBOTS_ANALYSIS_FILE_NAME, 'w', newline='')
    header = reader.fieldnames + ['domain-folders', 'n-domain-folders', 'nlu-files', 'n-nlu-files', 'n-nlu-yml', 'n-nlu-json', 'n-nlu-md', 'nlu-folders', 'n-nlu-folders', 'actions-files', 'n-actions-files', 'actions-folders', 'n-actions-folders', 'readme-files', 'n-readme-files', 'readme-folders', 'n-readme-folders', 'language-files', 'n-language-files', 'language-folders', 'n-language-folders']
    writer = csv.DictWriter(multi_file, delimiter=CSV_SEPARATOR, fieldnames=header)
    writer.writeheader()

    for chatbot_info in chatbots:

        zip_path = ZIP_FOLDER + '/' + chatbot_info['full-name'].replace('/', '_') + '.zip'

        repository =  zipfile.ZipFile(zip_path, 'r')

        chatbot_info['domain-files'] = ast.literal_eval(chatbot_info['domain-files'])

        domain_is_model = False
        domain_is_test = False

        chatbot_info['domain-folders'] = []

        for domain in chatbot_info['domain-files']:
            if 'test' in domain:
                    domain_is_test = True
            if 'models/dialogue' in domain:
                    domain_is_model = True
            if str(Path(domain).parent) not in chatbot_info['domain-folders']:
                chatbot_info['domain-folders'].append(str(Path(domain).parent))
        
        chatbot_info['n-domain-folders'] = len(chatbot_info['domain-folders'])


        chatbot_info = find_nlu_files(repository, chatbot_info, domain_is_test, domain_is_model)
        chatbot_info = find_action_files(repository, chatbot_info, domain_is_test, domain_is_model)
        chatbot_info = find_readme_files(repository, chatbot_info, domain_is_test, domain_is_model)
        chatbot_info = find_language_files(repository, chatbot_info, domain_is_test, domain_is_model)
        writer.writerow(chatbot_info)
    
    chatbot_file.close()
    multi_file.close()


main()
