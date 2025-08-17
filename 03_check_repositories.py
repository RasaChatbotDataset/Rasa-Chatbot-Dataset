import csv
import zipfile
import re
from utils import download_zip_no_timeout, download_zip_timeout, clean_zip
import os
from utils import sync
import shutil
import argparse
from multiprocessing import Process, Queue, freeze_support
import requests
import time


INPUT_FOLDER = os.path.join('results', '02_results')
REPOSITORIES_FILE = 'repositories_commit.csv'
RESULTS_FOLDER = os.path.join('results', '03_results')
CHATBOTS_FILE = 'chatbot_repositories.csv'
NOT_CHATBOTS_FILE = 'not_chatbot_repositories.csv'
NOT_INDEXED_REPO_FILE = 'not_indexed_repositories.csv'
NOT_FOUND_REPOSITORIES_FILE = 'not_found_repositories.csv'
ZIP_DIRECTORY = 'chatbot_repositories_zip'
CSV_SEPARATOR= ';'
TIMEOUT_REPO_FILE = 'timeout_repositories.csv'

    

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
                #print(f"Decode error")
                continue
    return domain_files

# Handle download zip with timeout
def handle_download_zip_timeout(zip_directory, repo_name, commit, timeout):
    queue = Queue()
    p = Process(target=download_zip_timeout, args=(zip_directory, repo_name, commit, queue))
    p.start()
    p.join(timeout)
    
    if p.is_alive():
        p.terminate()
        p.join()
        print(f"{repo_name}: timeout in ZIP download, exceeded {timeout} seconds")
        return 0
    
    return queue.get() if not queue.empty() else -1


def main():

    # Optional argument for number of repositories and timeout
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument(
        "--n-repos",
        type=int,
        default=-1,
        help="Number of repositories (default: all)"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=-1,
        help="Timeout for zip download (default: none)"
    )

    args = parser.parse_args()

    print('\n\n', '-'*20, 'REPOSITORY CLASSIFICATION', '-'*20, '\n')

    # Result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open file
    repo_file = open( os.path.join(INPUT_FOLDER, REPOSITORIES_FILE), 'r')
    reader = csv.DictReader(repo_file, delimiter=CSV_SEPARATOR)
    repositories = list(reader)
    
    # Open result files
    not_found_repo_file = open(os.path.join(RESULTS_FOLDER, NOT_FOUND_REPOSITORIES_FILE), 'w', newline='')
    not_found_csv = csv.DictWriter(not_found_repo_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
    not_found_csv.writeheader()

    ncb_file = open(os.path.join(RESULTS_FOLDER, NOT_CHATBOTS_FILE), 'w', newline='')
    ncb_csv = csv.DictWriter(ncb_file, fieldnames= reader.fieldnames, delimiter=CSV_SEPARATOR)
    ncb_csv.writeheader()

    cb_file = open(os.path.join(RESULTS_FOLDER, CHATBOTS_FILE), 'w', newline='')
    cb_headers =  reader.fieldnames + ['domain-files', 'n-domain-files']
    cb_csv = csv.DictWriter(cb_file, fieldnames=cb_headers, delimiter=CSV_SEPARATOR)
    cb_csv.writeheader()

    timeout_file = open(os.path.join(RESULTS_FOLDER, TIMEOUT_REPO_FILE), 'w', newline='')
    timeout_csv = csv.DictWriter(timeout_file, fieldnames= reader.fieldnames, delimiter=CSV_SEPARATOR)
    timeout_csv.writeheader()

    
    # Create zip folder if not already defined
    if not os.path.isdir(ZIP_DIRECTORY):
        os.makedirs(ZIP_DIRECTORY)

    # Repositories number check
    if args.n_repos >0 and args.n_repos < len(repositories):
        print(f'Number of repositories: {args.n_repos}\n')
        repositories = repositories[0:args.n_repos]
    else:
        print(f'Number of chatbots: {len(repositories)} (all)\n')
    
    # Timeout check
    if args.timeout > 0:
        print(f'Zip download timeout: {args.timeout}')
    else:
        print('Zip download timeout: no timeout')

    # Counters
    n_c_repos = 0
    n_nc_repos = 0
    n_nf_repos = 0
    n_t_repos = 0
    
    # For each repository
    for i in range(len(repositories)): 
        connection_retries = 0
        repo = repositories[i]
        # Periodical sync
        if i%50==0:
            print(f"> Processed repositories: {i}/{len(repositories)}\n")
            cb_file.flush()
            ncb_file.flush()
            not_found_repo_file.flush()
            timeout_file.flush()
            #sync(ZIP_DIRECTORY)
            #print('sync')
        try:
            # Download zip
            if args.timeout > 0:
                zip_path = handle_download_zip_timeout(ZIP_DIRECTORY, repo['full-name'], repo['last-commit'], args.timeout)
            else:
                zip_path = download_zip_no_timeout(ZIP_DIRECTORY, repo['full-name'], repo['last-commit'])

            # Timeout error
            if zip_path == 0:
                timeout_csv.writerow(repo)
                n_t_repos += 1
                # Remove zip
                #os.remove(zip_path) 

            # Not found error
            elif zip_path == -1:
                print(f"Not Found repository: {repo['full-name']}")
                not_found_csv.writerow(repo)
                n_nf_repos += 1
            
            # Connection error
            elif zip_path == -2:
                print('Connection error: sleep for 30 seconds')
                time.sleep(30)
                i = i - 1
                connection_retries += 1
                if connection_retries == 5:
                    print('Too many connection retries: connection persistent error, process terminated')
                    break
            
            # Repository downloaded
            else:
                # Chatbot check
                domain_files = find_keyword_in_repo('intents', zip_path, repo['last-commit'])
                # Not chatbot
                if not domain_files:
                    print(f"{repo['full-name']}: not chatbot")
                    ncb_csv.writerow(repo)
                    # Remove zip
                    os.remove(zip_path) 
                    n_nc_repos += 1
                else:
                    # Chatbot
                    print(f"{repo['full-name']}: chatbot")
                    repo['domain-files'] = domain_files
                    repo['n-domain-files'] = len(domain_files)
                    cb_csv.writerow(repo)
                    # Clean zip
                    clean_zip(zip_path)
                    n_c_repos += 1

        # Exception: not_found repository
        except zipfile.BadZipFile as e:
            print(f"Not Found repository: {repo['full-name']}")
            not_found_csv.writerow(repo)
            #os.remove(zip_path)
    print(f"\n> Processed repositories: {len(repositories)}/{len(repositories)}")
    print('Step 3 completed\n')
    print(f'CHATBOT REPOSITORIES: {n_c_repos}\nNON CHATBOT REPOSITORIES: {n_nc_repos}\nNOT FOUND REPOSITORIES: {n_nf_repos}\nTIMEOUT REPOSITORIES: {n_t_repos}')

    
    cb_file.close()
    ncb_file.close()
    not_found_repo_file.close()
    timeout_file.close()
    #sync(ZIP_DIRECTORY)


if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()
