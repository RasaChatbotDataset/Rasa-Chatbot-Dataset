import csv
import zipfile
import re
from utils import download_zip, clean_zip
import os
from utils import sync
import shutil


RESULTS_FOLDER ='results/05_results'
OLD_RESULTS_FOLDER = 'results/03_results'
NOT_INDEXED_FILE_NAME = OLD_RESULTS_FOLDER +'/not_indexed_repositories.csv'
CSV_SEPARATOR = ';'
CHATBOTS_FILE = 'chatbot_repositories.csv'
NOT_CHATBOTS_FILE = 'not_chatbot_repositories.csv'
NOT_FOUND_REPOSITORIES_FILE = 'not_found_repositories.csv'
ZIP_DIRECTORY = 'chatbot_repositories_zip'

    

# Check if repository is chatbot
def find_keyword_in_repo(keyword, repo_zip_path, commit):
    domain_files = []
    repo =  zipfile.ZipFile(repo_zip_path, 'r')
    r = re.compile(".*.yml")
    yml_list = list(filter(r.match, repo.namelist()))
    for file_path in yml_list:
        with repo.open(file_path) as yml_file:
            try:
                yml_content = yml_file.read().decode()
                if keyword in yml_content:
                    domain_files.append(file_path.split(commit+'/')[-1])
            except UnicodeDecodeError as e:
                print(f"Decode error")
    return domain_files



def main():

    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open files
    not_indexed_file = open(NOT_INDEXED_FILE_NAME, 'r')
    reader = csv.DictReader(not_indexed_file, delimiter=CSV_SEPARATOR)
    repositories = list(reader)
    
    shutil.copy(OLD_RESULTS_FOLDER+'/'+CHATBOTS_FILE, RESULTS_FOLDER+'/'+CHATBOTS_FILE)
    shutil.copy(OLD_RESULTS_FOLDER+'/'+NOT_CHATBOTS_FILE, RESULTS_FOLDER+'/'+NOT_CHATBOTS_FILE)

    if os.path.isfile(OLD_RESULTS_FOLDER+'/'+NOT_FOUND_REPOSITORIES_FILE):
        shutil.copy(OLD_RESULTS_FOLDER+'/'+NOT_FOUND_REPOSITORIES_FILE, RESULTS_FOLDER+'/'+NOT_FOUND_REPOSITORIES_FILE)
        not_found_repo_file = open(RESULTS_FOLDER+'/'+NOT_FOUND_REPOSITORIES_FILE, 'a', newline='')
        not_found_csv = csv.DictWriter(not_found_repo_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
    else:
        not_found_repo_file = open(RESULTS_FOLDER+'/'+NOT_FOUND_REPOSITORIES_FILE, 'w', newline='')
        not_found_csv = csv.DictWriter(not_found_repo_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
        not_found_csv.writeheader()


    ncb_file = open(RESULTS_FOLDER+'/'+NOT_CHATBOTS_FILE, 'a', newline='')
    ncb_csv = csv.DictWriter(ncb_file, fieldnames= reader.fieldnames, delimiter=CSV_SEPARATOR)


    cb_file = open(RESULTS_FOLDER+'/'+CHATBOTS_FILE, 'a', newline='')
    cb_headers =  reader.fieldnames + ['domain-files']
    cb_csv = csv.DictWriter(cb_file, fieldnames=cb_headers, delimiter=CSV_SEPARATOR)
    
    if not os.path.isdir(ZIP_DIRECTORY):
        os.makedirs(ZIP_DIRECTORY)
    i=0
    for repo in repositories: 
        i += 1
        if i%50==0:
          #sync(ZIP_DIRECTORY)
          print('sync')
        try:
            # Download zip
            zip_path = download_zip(ZIP_DIRECTORY, repo['full-name'], repo['last-commit'])
            print('Download completed')
            if zip_path != -1:
                # Chatbot check
                domain_files = find_keyword_in_repo('intents', zip_path, repo['last-commit'])
                # Not chatbot
                if not domain_files:
                    print(f"{repo['full-name']}: not chatbot")
                    ncb_csv.writerow(repo)
                    #Remove zip
                    os.remove(zip_path) 
                else:
                    # Chatbot
                    print(f"{repo['full-name']}: chatbot")
                    repo['domain-files'] = domain_files
                    cb_csv.writerow(repo)
                    # Clean zip
                    clean_zip(zip_path)

        # Exception: not_found repository
        except zipfile.BadZipFile as e:
            print(f"Not Found repository: {e}")
            not_found_csv.writerow(repo)
            not_found_repo_file.close()
            #os.remove(zip_path)

    cb_file.close()
    ncb_file.close()
    #sync(ZIP_DIRECTORY)

main()
