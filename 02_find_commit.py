import requests
from dotenv import dotenv_values
import csv
import os

config = dotenv_values('config.env')


GITHUB_API_URL = "https://api.github.com"
ACCESS_TOKEN = config['GITHUB_TOKENS'].split(',')[0]
USER_AGENT = 'agent' 
RESULTS_FOLDER = 'results/02_results'
REPOSITORIES_FILE = 'results/01_results/repositories.csv'
CSV_SEPARATOR= ';'
COMMIT_REPO_FILE =  RESULTS_FOLDER + '/' + 'repositories_commit.csv'
EMPTY_REPOSITORIES = RESULTS_FOLDER + '/' + 'empty_repositories.csv'
  

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': USER_AGENT
}


def find_last_commit_sha(repo_name, branch):

    url = f"https://api.github.com/repos/{repo_name}/branches/{branch}"
    

    response = requests.get(url, headers=headers)
    return response 




def add_last_commit():

    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    repo_file = open(REPOSITORIES_FILE, 'r')
    reader = csv.DictReader(repo_file, delimiter=CSV_SEPARATOR)
    repos = list(reader)

    repo_complete_file = open(COMMIT_REPO_FILE, 'a', newline='')
    cheaders = reader.fieldnames + ['last-commit', 'last-commit-date']
    writer = csv.DictWriter(repo_complete_file, fieldnames=cheaders, delimiter=CSV_SEPARATOR)
    writer.writeheader()

    empty_file = open(EMPTY_REPOSITORIES, 'a', newline='')
    empty_writer = csv.DictWriter(empty_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
    empty_writer.writeheader()
    i = 0

    for repo in repos:
        i += 1
        if i%100 == 0:
            print(f"{i}/{len(repos)}")
            repo_complete_file.flush()
            empty_file.flush()

        response = find_last_commit_sha(repo['full-name'], repo['default-branch'])
        if response.status_code == 200:
            branch = response.json()
            commit = branch['commit']['sha']
            date = branch['commit']['commit']['author']['date']
            repo['last-commit'] = commit
            repo['last-commit-date'] = date
            writer.writerow(repo)
        elif response.status_code == 404:
            print(f"Error: {response} for repo {repo['full-name']}")
            empty_writer.writerow(repo)

        else:
            print(f"Error: {response} for repo {repo['full-name']}")
            quit()
    
    repo_file.close()
    repo_complete_file.close()
    empty_file.close()


add_last_commit()
