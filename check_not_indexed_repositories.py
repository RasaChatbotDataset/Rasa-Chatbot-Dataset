import requests
import csv
import zipfile
import re


NOT_INDEXED_FILE_NAME = "not_indexed.csv"
CSV_SEPARATOR = ';'
CHATBOTS_FILE = 'chatbots.csv'
NOT_CHATBOTS_FILE = 'not_chatbots.csv'
EMPTY_REPOSITORIES_FILE = 'empy_repositories'
import os

# Download GitHub repository
def download_zip(repo_name, branch):
    download_url = f"https://github.com/{repo_name}/archive/refs/heads/{branch}.zip"
    print(download_url)
    
    try: 
        response = requests.get(download_url, timeout=300)
        if response.status_code != 200:
            print(f'Error in repository {repo_name} ZIP download: {response.status_code}')
            return -1
        else:
            zip_path = f"chatbot_zip/{repo_name.replace('/', '_')}.zip"
            with open(zip_path, "wb") as f:
                f.write(response.content)
            return zip_path
    except requests.exceptions.Timeout:
        print(f"Timeout in repository {repo_name} ZIP download")
        return 0
    

# Clean zip from cache and models (except most recent)


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

    not_indexed_file = open(NOT_INDEXED_FILE_NAME, 'r')
    reader = csv.DictReader(not_indexed_file, delimiter=CSV_SEPARATOR)
    repositories = list(reader)


    ncb_file = open(NOT_CHATBOTS_FILE, 'a', newline='')
    ncb_csv = csv.DictWriter(ncb_file, fieldnames= reader.fieldnames, delimiter=CSV_SEPARATOR)

    cb_file = open(CHATBOTS_FILE, 'a', newline='')
    cb_headers =  reader.fieldnames + ['domain-files']
    cb_csv = csv.DictWriter(cb_file, fieldnames=cb_headers, delimiter=CSV_SEPARATOR)
    
    

    for repo in repositories[300:400]:
        try:
            zip_path = download_zip(repo['full-name'], repo['default-branch'])
            print('Download completed')
            if zip_path != -1:
                domain_files = find_keyword_in_repo('intents', zip_path)
                print(domain_files)
                if not domain_files:
                    print(f"{repo['full-name']}: not chatbot")
                    ncb_csv.writerow(repo)
                    ncb_file.flush()
                    os.remove(zip_path)
                else:
                    print(f"{repo['full-name']}: chatbot")
                    repo['domain-files'] = domain_files
                    cb_csv.writerow(repo)
                    cb_file.flush()
        except zipfile.BadZipFile as e:
            print(f"Empty repository: {e}")
            empty_repo_file = open(EMPTY_REPOSITORIES_FILE, 'a', newline='')
            empty_csv = csv.DictWriter(empty_repo_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
            empty_csv.writerow(repo)
            empty_repo_file.close()

    cb_file.close()
    ncb_file.close()


main()
