import zipfile
import csv
import yaml
import ast
import os
from utils import sync


RESULTS_FOLDER = 'results/06_results'
CHATBOTS_BEFORE_CLEAN_NAME=  'results/05_results/chatbot_repositories.csv'
CHATBOTS_FILE_NAME = RESULTS_FOLDER + '/' + 'chatbot_repositories.csv'
NO_MORE_DOMAIN_FILE_NAME = RESULTS_FOLDER + '/' + 'discarded_repositories.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
CHECK_DOMAIN_STATISTICS_FILE = RESULTS_FOLDER + '/' + 'clean_domain_statistics.txt'


# Clean wrong domain files
def check_domain_files(repository, chatbot_info):

    n_cleaned = 0
    chatbot_info['domain-files'] = ast.literal_eval(chatbot_info['domain-files']) 

    clean_domain_files = []
    tests_md = []

    for domain_file in chatbot_info['domain-files']:

        full_domain_path = chatbot_info['full-name'].split('/')[-1]+'-'+chatbot_info['last-commit']+ '/' + domain_file

        # Discard other rasa configuration files - other files
        if 'nlu.yml' in domain_file or 'stories.yml' in domain_file or 'rules.yml' in domain_file or 'docker-compose.yml' in domain_file:
            continue

        # Discard programming language libraries
        if 'node_modules' in domain_file or 'site-packages' in domain_file or 'vendor/' in domain_file or 'assets/libs' in domain_file:
            continue

        with repository.open(full_domain_path) as d_file:
            try:
                content = d_file.read().decode()
                domain = yaml.safe_load(content)

                # Not a domain file
                if 'intents' not in domain:
                    continue

            except:
                # YML parsing failed: not working file
                print('YML EXCEPTION')
                continue
        
        # Test files - copy files
        if 'test' in domain_file or 'models/dialogue' in domain_file:
            tests_md.append(domain_file)
        else:
            clean_domain_files.append(domain_file)
    
    if len(clean_domain_files) == 0 and len(tests_md) != 0:
            n_cleaned = len(chatbot_info['domain-files'])- len(tests_md)
            chatbot_info['domain-files'] = tests_md

    else:       
        n_cleaned = len(chatbot_info['domain-files']) - len(clean_domain_files)
        chatbot_info['domain-files'] = clean_domain_files

    return  chatbot_info, n_cleaned



def write_statistics(n_domain_removed, n_repository_cleaned, n_repository_removed):
    statistics_file = open(CHECK_DOMAIN_STATISTICS_FILE, 'w', newline='')
    statistics_file.write(f"Domain files removed: {n_domain_removed}\n")
    statistics_file.write(f"Repositories cleaned: {n_repository_cleaned}\n")
    statistics_file.write(f"Repositories removed: {n_repository_removed}\n")
    statistics_file.close()


def main():

    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    chatbot_file = open(CHATBOTS_BEFORE_CLEAN_NAME, 'r')
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    cleaned_file = open(CHATBOTS_FILE_NAME, 'w', newline='')
    analysis_writer = csv.DictWriter(cleaned_file, delimiter=CSV_SEPARATOR, fieldnames=reader.fieldnames)
    analysis_writer.writeheader()

    discarded_file = open(NO_MORE_DOMAIN_FILE_NAME, 'w', newline='')
    discarded_writer = csv.DictWriter(discarded_file, delimiter=CSV_SEPARATOR, fieldnames=reader.fieldnames)
    discarded_writer.writeheader()

    n_domain_removed = 0
    n_repository_cleaned = 0
    n_repository_removed = 0

    for chatbot_info in chatbots:

        zip_path = ZIP_FOLDER + '/' + chatbot_info['full-name'].replace('/', '_') + '.zip'
        try:
            repository =  zipfile.ZipFile(zip_path, 'r')
        except:
            print(chatbot_info['full-name'])
            continue

        chatbot_info, n = check_domain_files(repository, chatbot_info)

        if n>0:
            n_repository_cleaned += 1
            n_domain_removed += n
        
        chatbot_info['n-domain-files'] = len(chatbot_info['domain-files'])
        
        # If there is no domain file left: not a chatbot, remove zip
        if len(chatbot_info['domain-files']) > 0:
            analysis_writer.writerow(chatbot_info)
        else:
            n_repository_removed += 1
            discarded_writer.writerow(chatbot_info)
            os.remove(zip_path) 
    
    # Sync folder with google drive folder
    #sync(ZIP_FOLDER)
    cleaned_file.close()
    chatbot_file.close()
    discarded_file.close()

    write_statistics(n_domain_removed, n_repository_cleaned, n_repository_removed)


main()

