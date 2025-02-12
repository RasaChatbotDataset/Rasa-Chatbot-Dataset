import zipfile
import ast
import csv
import re
import yaml
import json
from pathlib import Path

CHATBOTS_FILE_NAME = 'chatbots-2025.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_zip-2025'
CHATBOTS_ANALYSIS_FILE_NAME = 'chatbots-2025-files.csv'

def find_nlu_files(repository, chatbot_info): 

    file_list = repository.namelist()

    # NLU files information
    chatbot_info['nlu-files'] = []
    chatbot_info['n-nlu-yml'] = 0
    chatbot_info['n-nlu-md'] = 0
    chatbot_info['n-nlu-json'] = 0
    chatbot_info['n-nlu-files'] = 0
    chatbot_info['nlu-folders'] = []
    chatbot_info['n-nlu-folders'] = 0


    for file in file_list:
        if 'node_modules' not in file and 'site-packages' not in file:
            if file.endswith('.yml') and not file.endswith('docker-compose.yml'):
                with repository.open(file) as nlu_file:
                    try:
                        content = nlu_file.read().decode()
                        try:
                            yml_content = yaml.safe_load(content)
                            if 'nlu' in yml_content:
                                clean_file_name = file.split(chatbot_info['last-commit']+'/')[-1]
                                chatbot_info['nlu-files'].append(clean_file_name)
                                chatbot_info['n-nlu-yml'] += 1

                                if str(Path(clean_file_name).parent) not in chatbot_info['nlu-folders']:
                                    chatbot_info['nlu-folders'].append(str(Path(clean_file_name).parent))
                                    chatbot_info['n-nlu-folders'] +=1
                        except Exception as e:
                            print('YML open error')
                    except:
                        print(f"Decode error")

            elif file.endswith('.json'):
                with repository.open(file) as nlu_file:
                    try:
                        content = nlu_file.read().decode()
                        try:
                            json_content = json.loads(content)
                            if 'rasa_nlu_data' in json_content:
                                clean_file_name = file.split(chatbot_info['last-commit']+'/')[-1]
                                chatbot_info['nlu-files'].append(clean_file_name)
                                chatbot_info['n-nlu-json'] +=1

                                if str(Path(clean_file_name).parent) not in chatbot_info['nlu-folders']:
                                    chatbot_info['nlu-folders'].append(str(Path(clean_file_name).parent))
                                    chatbot_info['n-nlu-folders'] +=1
                        except Exception as e:
                            print('Json parsing error')
                    except:
                        print(f"Decode error")
                
            elif file.endswith('.md'):
                with repository.open(file) as nlu_file:
                    try:
                        content = nlu_file.read().decode()
                        if '## intent:' in content:
                            clean_file_name = file.split(chatbot_info['last-commit']+'/')[-1]
                            if str(Path(clean_file_name).parent) not in chatbot_info['nlu-folders']:
                                chatbot_info['nlu-folders'].append(str(Path(clean_file_name).parent))

                            chatbot_info['nlu-files'].append(clean_file_name)
                            chatbot_info['n-nlu-md'] +=1

                    except UnicodeDecodeError as e:
                        print(f"Decode error")

        
    chatbot_info['n-nlu-files'] = len(chatbot_info['nlu-files'])
    chatbot_info['n-nlu-folders'] = len(chatbot_info['nlu-folders'])

    return chatbot_info


def find_action_files(repository, chatbot_info):

    file_list = repository.namelist()

    file_regex = re.compile(".*/actions\\.py$")
    folder_regex = re.compile(".*/actions/.*\\.py$")

    actions_file_list = list(filter(file_regex.match, file_list))
    actions_file_list += list(filter(folder_regex.match, file_list))
    actions_file_list = set(actions_file_list)

    chatbot_info['actions-files'] = []
    chatbot_info['actions-folders'] = []
    chatbot_info['n-actions-files'] = 0
    chatbot_info['n-actions-folders'] = 0
    chatbot_info['actions-folders'] = []

    for file in actions_file_list:
        if 'node_modules' not in file and 'site-packages' not in file:
            with repository.open(file) as action_file:
                try:
                    content = action_file.read().decode()  # vedere cosa succede con un file vuoto
                    empty = False
                    if len(content) == 0:
                        empty = True
                    
                    all_comment = True

                    for line in content:
                        if not line.startswith('#'):
                            all_comment = False

                    
                    if not all_comment and not empty and not file.endswith('__init__.py'):
                        clean_file_name = file.split(chatbot_info['last-commit']+'/')[-1]
                        chatbot_info['actions-files'].append(clean_file_name)

                        if str(Path(clean_file_name).parent) not in chatbot_info['actions-folders']:
                                    chatbot_info['actions-folders'].append(str(Path(clean_file_name).parent))
                                    
                
                except UnicodeDecodeError as e:
                        print(f"Decode error")
    

                    
    
    chatbot_info['n-actions-files'] = len(chatbot_info['actions-files'])
    chatbot_info['n-actions-folders'] = len(chatbot_info['actions-folders'])

    return chatbot_info


def find_readme_files(repository, chatbot_info):

    chatbot_info['readme-files'] = []
    chatbot_info['n-readme-files'] = 0

    file_list = repository.namelist()
    readme_regex = re.compile(".*README\\.md$")
    readme_file_list = list(filter(readme_regex.match, file_list))
    for readme in readme_file_list:
        clean_file_name = readme.split(chatbot_info['last-commit']+'/')[-1]
        if not 'site-packages' in readme and not 'node_modules' in readme:
            chatbot_info['readme-files'].append(clean_file_name)
    chatbot_info['n-readme-files'] = len(chatbot_info['readme-files'])

    return chatbot_info


def main():

    chatbot_file = open(CHATBOTS_FILE_NAME, 'r')
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    multi_file = open(CHATBOTS_ANALYSIS_FILE_NAME, 'w', newline='')
    header = reader.fieldnames + ['n-domain-files', 'nlu-files', 'n-nlu-files', 'n-nlu-yml', 'n-nlu-json', 'n-nlu-md', 'nlu-folders', 'n-nlu-folders', 'actions-files', 'n-actions-files', 'actions-folders', 'n-actions-folders', 'readme-files', 'n-readme-files']
    writer = csv.DictWriter(multi_file, delimiter=CSV_SEPARATOR, fieldnames=header)
    writer.writeheader()

    for chatbot_info in chatbots:

        zip_path = ZIP_FOLDER + '/' + chatbot_info['full-name'].replace('/', '_') + '.zip'

        repository =  zipfile.ZipFile(zip_path, 'r')

        chatbot_info['domain-files'] = ast.literal_eval(chatbot_info['domain-files'])
        chatbot_info['n-domain-files'] = len(chatbot_info['domain-files'])
        chatbot_info = find_nlu_files(repository, chatbot_info)
        chatbot_info = find_action_files(repository, chatbot_info)
        chatbot_info = find_readme_files(repository, chatbot_info)
        writer.writerow(chatbot_info)
    
    chatbot_file.close()
    multi_file.close()


main()
