import csv
import zipfile
import re
from utils import download_zip, clean_zip
import os
from utils import sync
import shutil


INPUT_FOLDER = 'results/02_results'
REPOSITORIES_FILE = 'repositories_commit.csv'
RESULTS_FOLDER = 'results/03_results_prova'
CHATBOTS_FILE = 'chatbot_repositories.csv'
NOT_CHATBOTS_FILE = 'not_chatbot_repositories.csv'
NOT_INDEXED_REPO_FILE = 'not_indexed_repositories.csv'
NOT_FOUND_REPOSITORIES_FILE = 'not_found_repositories.csv'
ZIP_DIRECTORY = 'chatbot_repositories_zip'
CSV_SEPARATOR= ';'

    

# Check if repository is chatbot
def find_keyword_in_repo(keyword, repo_zip_path, commit):
    domain_files = []
    repo =  zipfile.ZipFile(repo_zip_path, 'r')

    # Find all YML files
    r = re.compile(".*.yml")
    yml_list = list(filter(r.match, repo.namelist()))

    # Check each file
    for file_path in yml_list:
        with repo.open(file_path) as yml_file:
            try:
                # Decode file
                yml_content = yml_file.read().decode()
                # If "intent" in file: domain file
                if keyword in yml_content:
                    domain_files.append(file_path.split(commit+'/')[-1])
            except UnicodeDecodeError as e:
                print(f"Decode error")
    return domain_files



def main():

    # Result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open file
    repo_file = open(   INPUT_FOLDER + '/' +REPOSITORIES_FILE, 'r')
    reader = csv.DictReader(repo_file, delimiter=CSV_SEPARATOR)
    repositories = list(reader)
    
    # Open result files
    not_found_repo_file = open(RESULTS_FOLDER+'/'+NOT_FOUND_REPOSITORIES_FILE, 'w', newline='')
    not_found_csv = csv.DictWriter(not_found_repo_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
    not_found_csv.writeheader()

    ncb_file = open(RESULTS_FOLDER+'/'+NOT_CHATBOTS_FILE, 'w', newline='')
    ncb_csv = csv.DictWriter(ncb_file, fieldnames= reader.fieldnames, delimiter=CSV_SEPARATOR)
    ncb_csv.writeheader()

    cb_file = open(RESULTS_FOLDER+'/'+CHATBOTS_FILE, 'w', newline='')
    cb_headers =  reader.fieldnames + ['domain-files']
    cb_csv = csv.DictWriter(cb_file, fieldnames=cb_headers, delimiter=CSV_SEPARATOR)
    cb_csv.writeheader()

    
    # Create zip folder if not already defined
    if not os.path.isdir(ZIP_DIRECTORY):
        os.makedirs(ZIP_DIRECTORY)
    i=0
    # For each repository
    for repo in repositories: 
        i += 1
        # Periodical sync
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
                    # Remove zip
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
            #os.remove(zip_path)

    cb_file.close()
    ncb_file.close()
    not_found_repo_file.close()
    #sync(ZIP_DIRECTORY)

main()
