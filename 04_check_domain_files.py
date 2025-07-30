import zipfile
import csv
import yaml
import ast
import os
from utils import sync
import argparse


RESULTS_FOLDER = os.path.join('results', '04_results')
CHATBOTS_BEFORE_CLEAN_NAME=  os.path.join('results', '03_results', 'chatbot_repositories.csv')
CHATBOTS_FILE_NAME = os.path.join(RESULTS_FOLDER, 'chatbot_repositories.csv')
NO_MORE_DOMAIN_FILE_NAME = os.path.join(RESULTS_FOLDER, 'discarded_repositories.csv')
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
CHECK_DOMAIN_STATISTICS_FILE = os.path.join(RESULTS_FOLDER, 'clean_domain_statistics.txt')


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
    
    # Keep test files if they are the only ones
    if len(clean_domain_files) == 0 and len(tests_md) != 0:
            n_cleaned = len(chatbot_info['domain-files'])- len(tests_md)
            chatbot_info['domain-files'] = tests_md

    else:       
        n_cleaned = len(chatbot_info['domain-files']) - len(clean_domain_files)
        chatbot_info['domain-files'] = clean_domain_files

    return  chatbot_info, n_cleaned


# Save statistics about domain cleaning
def write_statistics(n_domain_removed, n_repository_cleaned, n_repository_removed):
    statistics_file = open(CHECK_DOMAIN_STATISTICS_FILE, 'w', newline='')
    statistics_file.write(f"Domain files removed: {n_domain_removed}\n")
    statistics_file.write(f"Repositories cleaned: {n_repository_cleaned}\n")
    statistics_file.write(f"Repositories removed: {n_repository_removed}\n")
    statistics_file.close()

# Print statistics about domain cleaning
def print_statistics(n_domain_removed, n_repository_cleaned, n_repository_removed):
    print(f"DOMAIN FILES REMOVED: {n_domain_removed}\n")
    print(f"REPOSITORIES CLEANED: {n_repository_cleaned}\n")
    print(f"REPOSITORIES REMOVED: {n_repository_removed}\n")


def main():

    # Result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

     # Optional argument for number of repositories
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument(
        "--n-repos",
        type=int,
        default=-1,
        help="Number of chatbot repositories (default: all)"
    )

    args = parser.parse_args()

    print('\n\n', '-'*20, 'DOMAIN FILES FILTERING', '-'*20, '\n')

    # Open files
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

    # Chatbot repositories number check
    if args.n_repos > 0 and args.n_repos < len(chatbots):
        print(f'Number of chatbot repositories: {args.n_repos}\n')
        chatbots = chatbots[0:args.n_repos]
    else:
        print(f'Number of chatbots: {len(chatbots)} (all)\n')

    for i in range(len(chatbots)):

        if i%50==0:
            print(f'> Processed repositories: {i}/{len(chatbots)}')

        chatbot_info = chatbots[i]

        # Open zip file
        zip_path = os.path.join(ZIP_FOLDER, chatbot_info['full-name'].replace('/', '_') + '.zip')
        try:
            repository =  zipfile.ZipFile(zip_path, 'r')
        except Exception as e:
            print(f"{chatbot_info['full-name']}: exception {e}")
            continue

        # Clean domain files
        chatbot_info, n = check_domain_files(repository, chatbot_info)

        # Update statistics
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

    print(f'> Processed repositories: {len(chatbots)}/{len(chatbots)}')
    print('Step 4 completed')

    # Close files
    cleaned_file.close()
    chatbot_file.close()
    discarded_file.close()

    # Save statistics
    write_statistics(n_domain_removed, n_repository_cleaned, n_repository_removed)
    print_statistics(n_domain_removed, n_repository_cleaned, n_repository_removed)


main()

