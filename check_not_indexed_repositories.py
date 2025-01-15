import requests
import csv
import zipfile
import re
from utils import download_zip, clean_zip
import os


NOT_INDEXED_FILE_NAME = "not_indexed-2025.csv"
CSV_SEPARATOR = ';'
CHATBOTS_FILE = 'chatbots-2025.csv'
NOT_CHATBOTS_FILE = 'not_chatbots-2025.csv'
EMPTY_REPOSITORIES_FILE = 'empty_repositories-2025-csv'
ZIP_DIRECTORY = 'chatbot_zip-2025'

    

# Check if repository is chatbot
def find_keyword_in_repo(keyword, repo_zip_path):
    domain_files = []
    repo =  zipfile.ZipFile(repo_zip_path, 'r')
    r = re.compile(".*.yml")
    yml_list = list(filter(r.match, repo.namelist()))
    for file_path in yml_list:
        with repo.open(file_path) as yml_file:
            try:
                yml_content = yml_file.read().decode()
                if keyword in yml_content:
                    domain_files.append(file_path)
            except UnicodeDecodeError as e:
                print(f"Decode error")
    return domain_files


def main():

    # Open files
    not_indexed_file = open(NOT_INDEXED_FILE_NAME, 'r')
    reader = csv.DictReader(not_indexed_file, delimiter=CSV_SEPARATOR)
    repositories = list(reader)

    ncb_file = open(NOT_CHATBOTS_FILE, 'a', newline='')
    ncb_csv = csv.DictWriter(ncb_file, fieldnames= reader.fieldnames, delimiter=CSV_SEPARATOR)

    cb_file = open(CHATBOTS_FILE, 'a', newline='')
    cb_headers =  reader.fieldnames + ['domain-files']
    cb_csv = csv.DictWriter(cb_file, fieldnames=cb_headers, delimiter=CSV_SEPARATOR)
    
    if not os.path.isdir(ZIP_DIRECTORY):
        os.makedirs(ZIP_DIRECTORY)

    for repo in repositories: 
        try:
            # Download zip
            zip_path = download_zip(ZIP_DIRECTORY, repo['full-name'], repo['last-commit'])
            print('Download completed')
            if zip_path != -1:
                # Chatbot check
                domain_files = find_keyword_in_repo('intents', zip_path)
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

        # Exception: empty repository
        except zipfile.BadZipFile as e:
            print(f"Empty repository: {e}")
            empty_repo_file = open(EMPTY_REPOSITORIES_FILE, 'a', newline='')
            empty_csv = csv.DictWriter(empty_repo_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
            empty_csv.writerow(repo)
            empty_repo_file.close()
            os.remove(zip_path)

    cb_file.close()
    ncb_file.close()


main()
