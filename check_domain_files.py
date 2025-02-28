import zipfile
import csv
import yaml
import ast
import os
from utils import sync

CHATBOTS_FILE_NAME = 'chatbots-2025.csv'
NO_MORE_DOMAIN_FILE_NAME = 'no-more-domain-chatbots-2025.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_zip-2025'
CHECK_DOMAIN_STATISTICS_FILE = 'clean_domain_statistics.txt'
CHATBOTS_CLEAN_FILE_NAME = 'chatbots-2025-clean.csv'


# Clean not domain files - not working domain files
def check_domain_files(repository, chatbot_info):

    chatbot_info['domain-files'] = ast.literal_eval(chatbot_info['domain-files']) 
    n_cleaned = 0
    

    for domain_file in chatbot_info['domain-files'][:]:
        full_domain_path = chatbot_info['full-name'].split('/')[-1]+'-'+chatbot_info['last-commit']+ '/' + domain_file
        with repository.open(full_domain_path) as nlu_file:
            try:
                content = nlu_file.read().decode()
                domain = yaml.safe_load(content)

                # Not a domain file
                if 'intents' not in domain:
                    chatbot_info['domain-files'].remove(domain_file)
                    n_cleaned += 1

            except:
                # YML parsing failed: not working file
                chatbot_info['domain-files'].remove(domain_file)

                n_cleaned += 1

    return  chatbot_info, n_cleaned



def write_statistics(n_domain_removed, n_repository_cleaned, n_repository_removed):
    statistics_file = open(CHECK_DOMAIN_STATISTICS_FILE, 'w', newline='')
    statistics_file.write(f"Domain files removed: {n_domain_removed}")
    statistics_file.write(f"Repositories cleaned: {n_repository_cleaned}")
    statistics_file.write(f"Repositories removed: {n_repository_removed}")
    statistics_file.close()


def main():

    chatbot_file = open(CHATBOTS_FILE_NAME, 'r')
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    cleaned_file = open(CHATBOTS_CLEAN_FILE_NAME, 'w', newline='')
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

        repository =  zipfile.ZipFile(zip_path, 'r')

        chatbot_info, n = check_domain_files(repository, chatbot_info)

        if n>0:
            n_repository_cleaned += 1
            n_domain_removed += n
        
        chatbot_info['domain-files'] = ast.literal_eval(chatbot_info['domain-files']) 
        chatbot_info['n-domain-files'] = len(chatbot_info['domain-files'])
        
        # If there is no domain file left: not a chatbot, remove zip
        if len(chatbot_info['domain-files']) > 0:
            analysis_writer.writerow(chatbot_info)
        else:
            n_repository_removed += 1
            discarded_writer.writerow(chatbot_info)
            os.remove(zip_path) 
    
    # Sync folder with google drive folder
    sync(ZIP_FOLDER)
    cleaned_file.close()
    chatbot_file.close()
    discarded_file.close()

    write_statistics(n_domain_removed, n_repository_cleaned, n_repository_removed)

    os.remove(CHATBOTS_FILE_NAME)
    os.rename(CHATBOTS_CLEAN_FILE_NAME, CHATBOTS_FILE_NAME)


main()

