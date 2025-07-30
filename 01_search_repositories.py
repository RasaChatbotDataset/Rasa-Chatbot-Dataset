import requests

from dotenv import dotenv_values
from datetime import datetime
import json
import os
import argparse


config = dotenv_values('config.env')


GITHUB_API_URL = "https://api.github.com"
ACCESS_TOKEN = config['GITHUB_TOKEN']
USER_AGENT = 'agent' 


REPO_KEYWORDS = ['rasa', 'chatbot'] 
RESULTS_FOLDER = os.path.join('results', '01_results')
RESULT_FILE = os.path.join(RESULTS_FOLDER, 'repositories.csv')
CSV_SEPARATOR= ';'
REPO_JSON_DIRECTORY =  os.path.join(RESULTS_FOLDER, 'repositories_json')
  

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': USER_AGENT
}

# Search repositories with keywords
def execute_query(keywords, page, dt):
    delimiter = "+"
    query = delimiter.join(keywords)
    search_url = f"{GITHUB_API_URL}/search/repositories?q={query}+in:name,description,topics,readme+pushed:<{dt.isoformat()}&sort=updated&page={page}&per_page=100"
    repo_response = requests.get(search_url, headers=headers)
    return repo_response

# Search chatbot repositories
def search_repositories():

    # Optional argument for number of chatbots
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument(
        "--n-repos",
        type=int,
        default=-1,
        help="Number of repositories (default: all)"
    )

    args = parser.parse_args()

    print('\n\n', '-'*20, 'REPOSITORY SEARCH', '-'*20, '\n')

    # Result folders creation
    if not os.path.isdir(RESULTS_FOLDER):
        os.makedirs(RESULTS_FOLDER)
    if not os.path.isdir(REPO_JSON_DIRECTORY):
        os.mkdir(REPO_JSON_DIRECTORY)

    # Repositories number check
    if args.n_repos >= 100:
        max_requests = (int) (args.n_repos / 100)
        print(f'Max number of repositories: {args.n_repos}\nMax number of requests: {max_requests}\n')
    else:
        max_requests = -1
        print(f'No max number of repositories set: seach process will cover all repositories\n')

    # Open files
    repo_file = open(RESULT_FILE, 'w')
    repo_file.write('full-name'+CSV_SEPARATOR+'html-url'+CSV_SEPARATOR+'stars'+CSV_SEPARATOR+'forks'+CSV_SEPARATOR
                    +'created-at'+CSV_SEPARATOR+'updated-at'+CSV_SEPARATOR+'pushed-at'+CSV_SEPARATOR +
                    'default-branch' + CSV_SEPARATOR +'owner-name'+CSV_SEPARATOR+'owner-id'+CSV_SEPARATOR+'owner-type'
                    + CSV_SEPARATOR + 'is-fork' + CSV_SEPARATOR + 'fork-parent\n')
    page = 1
    list_completed = False
    total_req= 0
    repo_counter = 0

    # Get min date: today
    dt = datetime.today()
    min_pushed_date = dt

    # Cover all repositories
    while not list_completed:

        # Search repositories with keywords and last update before dt
        repo_response =  execute_query(REPO_KEYWORDS, page, dt)
        total_req+= 1

        if repo_response.status_code != 200:
            print(f"Error in search: {repo_response.status_code}")
            break

        repositories = repo_response.json()

        # First page of results
        if page==1:
            print(f'Total requests: {total_req}')
            print(f"Total repositories pushed before {min_pushed_date}: {repositories['total_count']}")
        print(f'Page: {page}')


        # No more results
        if repositories is None or 'items' not in repositories:
            print('No repository found - Error in repository search')
            break

        # For each repository in the response
        for repo in repositories['items']:
            repo_counter += 1
            fork_parent = ''
            if repo['fork']:
                fork_parent = repo['parent']['full_name']
            
            # Write selected information on file
            repo_file.write(repo['full_name']+CSV_SEPARATOR+repo['html_url']+CSV_SEPARATOR+str(repo['stargazers_count'])+CSV_SEPARATOR+str(repo['forks_count'])+CSV_SEPARATOR
                        + repo['created_at'] + CSV_SEPARATOR + repo['updated_at'] + CSV_SEPARATOR + repo['pushed_at'] + CSV_SEPARATOR
                        + repo['default_branch'] + CSV_SEPARATOR
                        + repo['owner']['login']+CSV_SEPARATOR+str(repo['owner']['id'])+CSV_SEPARATOR+repo['owner']['type']+ CSV_SEPARATOR
                        + str(repo['fork'])+ CSV_SEPARATOR + fork_parent+'\n')
            
            single_repo_file = open(REPO_JSON_DIRECTORY+'/'+repo['full_name'].replace('/', '_')+'.json', 'w', newline='')
            json.dump(repo, single_repo_file)
            single_repo_file.close()
            
            if min_pushed_date > datetime.fromisoformat(repo['pushed_at'].rstrip('Z')):
                min_pushed_date = datetime.fromisoformat(repo['pushed_at'].rstrip('Z'))

        # Page number is 10: new request needed (GitHub limits results to 1000, with 100 per page)
        if page == 10:
            page = 1
            # Last update date update
            dt = min_pushed_date
        else:
            if 'next' in repo_response.links:
                page += 1
            else:
                list_completed = True
        
        # Max number of requests
        if total_req>= max_requests:
            list_completed = True

    repo_file.close()
    print('\nStep 1 completed')
    print('TOTAL REPOSITORIES: ',repo_counter)


search_repositories()
