import ast
import os
import pandas as pd
import yaml
import json
import zipfile
import re
import argparse

FILES = [os.path.join('results', '06_results', 'chatbot_repositories_sfsd.csv'), os.path.join('results', '06_results', 'chatbot_repositories_mfsd.csv'), os.path.join('results', '06_results', 'chatbot_repositories_sfmd.csv'), os.path.join('results', '06_results', 'chatbot_repositories_mfmd.csv')]
RESULTS_FOLDER = os.path.join('results', '10_results')
CHATBOT_FILE = os.path.join('results', '09_results', 'chatbots.csv')
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
PROGRAMMING_LANGUAGES = ['java', 'python', 'android', 'node_js', 'php', 'generic']



# Extract language from configuration file
def extract_config_language(chatbot):

    if chatbot['temp_row_index'] % 50 == 0:
        print(f"> Processed chatbots: {chatbot['temp_row_index']}")
    zip_path = os.path.join(ZIP_FOLDER, chatbot['full-name'].replace('/', '_') + '.zip')

    repository =  zipfile.ZipFile(zip_path, 'r')

    file_list = ast.literal_eval(chatbot['language-files'])
    languages = []

    for file in file_list:
        full_config_path = chatbot['full-name'].split('/')[-1]+'-'+chatbot['last-commit']+ '/' + file
        with repository.open(full_config_path) as config_file:
            try:
                content = config_file.read().decode()
                if file.endswith('.yml'):
                    content = yaml.safe_load(content)
                elif file.endswith('.json'):
                    content = json.loads(content)
                
                language = content['language']

                # Discard programming languages and nested configurations
                if language in PROGRAMMING_LANGUAGES or not isinstance(language, str):
                    continue

                # Replace training dataset name with language
                if 'core' in language or 'spacy' in language or 'model' in language:
                    language = language[:2]

                # Delete specifications
                if '{' in language:
                    language = re.sub(r'\{.*?\}', '', language)
                    if len(language) == 0:
                        continue

                if language not in languages:
                    languages.append(language)
                        
            except UnicodeDecodeError as e:
                print(f"Decode error")
            except Exception as e:
                print(f"Error for repository {chatbot['full-name']}, file {file}")
                print(e)

    return languages
           


def main():

    # Result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)
    
    # Optional argument for number of chatbots
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument(
        "--n-chatbots",
        type=int,
        default=-1,
        help="Number of chatbots (default: all)"
    )

    args = parser.parse_args()

    print('\n\n', '-'*20, 'CONFIGURATION LANGUAGE EXTRACTION', '-'*20, '\n') 

    # Open dataset as pandas dataframe
    chatbots = pd.read_csv(CHATBOT_FILE, sep=CSV_SEPARATOR)
    cb_files = pd.DataFrame()

    # Chatbot number check
    if args.n_chatbots >0 and args.n_chatbots < chatbots.shape[0]:
        chatbots = chatbots.head(args.n_chatbots)
        print(f'Number of chatbots: {args.n_chatbots}\n')
    else:
        print(f'Number of chatbots: {chatbots.shape[0]} (all)\n')

    # Join chatbot dataset with config file info
    for file in FILES:
        cb_with_files = pd.read_csv(file, sep=CSV_SEPARATOR)
        cb_with_files = cb_with_files[['id', 'language-files']]
        cb_files = pd.concat([cb_files, cb_with_files])

    chatbots = pd.merge(chatbots, cb_files, how='inner')

    chatbots.to_csv(os.path.join(RESULTS_FOLDER, 'chatbots_join_config_file.csv'), sep=CSV_SEPARATOR, index=False)
    
    chatbots['temp_row_index'] = range(len(chatbots))

    # Extract configuration language
    chatbots['config-languages'] = chatbots.apply(extract_config_language, axis=1)
    print(f'> Processed chatbots: {chatbots.shape[0]}/{chatbots.shape[0]}')

    # Remove columns
    chatbots = chatbots.drop('temp_row_index', axis=1)
    chatbots = chatbots.drop('n-language-files', axis=1)
    chatbots = chatbots.drop('language-files', axis=1)

    # Write dataset
    chatbots.to_csv(os.path.join(RESULTS_FOLDER, 'chatbots.csv'), sep=CSV_SEPARATOR, index=False)

    print('Step 10 completed')

main()