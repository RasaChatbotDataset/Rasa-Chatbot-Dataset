import requests
from dotenv import dotenv_values
import csv
import os
import argparse

config = dotenv_values('config.env')


GITHUB_API_URL = "https://api.github.com"
ACCESS_TOKEN = config['GITHUB_TOKEN']
USER_AGENT = 'agent' 
RESULTS_FOLDER = os.path.join('results','02_results')
REPOSITORIES_FILE = os.path.join('results', '01_results', 'repositories.csv')
CSV_SEPARATOR= ';'
COMMIT_REPO_FILE =  os.path.join(RESULTS_FOLDER, 'repositories_commit.csv')
EMPTY_REPOSITORIES = os.path.join(RESULTS_FOLDER, 'empty_repositories.csv')
  

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': USER_AGENT
}


# Retrieve last commit of a repository on a branch
def find_last_commit_sha(repo_name, branch):

    url = f"https://api.github.com/repos/{repo_name}/branches/{branch}"

    response = requests.get(url, headers=headers)
    return response 


# Add last commit info to all repositories
def add_last_commit():

    # Optional argument for number of chatbots
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument(
        "--n-repos",
        type=int,
        default=-1,
        help="Number of repositories (default: all)"
    )

    args = parser.parse_args()

    print('\n\n', '-'*20, 'LAST COMMIT RETRIEVAL', '-'*20, '\n')


    # Result folder creation
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open files
    repo_file = open(REPOSITORIES_FILE, 'r')
    reader = csv.DictReader(repo_file, delimiter=CSV_SEPARATOR)
    repos = list(reader)

    repo_complete_file = open(COMMIT_REPO_FILE, 'w', newline='')
    cheaders = reader.fieldnames + ['last-commit', 'last-commit-date']
    writer = csv.DictWriter(repo_complete_file, fieldnames=cheaders, delimiter=CSV_SEPARATOR)
    writer.writeheader()

    empty_file = open(EMPTY_REPOSITORIES, 'w', newline='')
    empty_writer = csv.DictWriter(empty_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
    empty_writer.writeheader()

    # Repositories number check
    if args.n_repos >0 and args.n_repos < len(repos):
        print(f'Number of repositories: {args.n_repos}\n')
        repos = repos[0:args.n_repos]
    else:
        print(f'Number of chatbots: {len(repos)} (all)\n')


    # For each repository
    for i in range(len(repos)):
        repo = repos[i]

        # Periodically update files
        if i%50 == 0:
            print(f">Processed repositories: {i}/{len(repos)}")
            repo_complete_file.flush()
            empty_file.flush()

        # Retrieve last commit sha and date
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
    
    print(f'> Processed repositories: {len(repos)}/{len(repos)}')
    print('Step 2 completed')
    
    # Close files
    repo_file.close()
    repo_complete_file.close()
    empty_file.close()


add_last_commit()
