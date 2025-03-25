import requests
import threading

from dotenv import dotenv_values
import csv
import time
import sys 
import os
config = dotenv_values('config.env')


GITHUB_API_URL = "https://api.github.com"
ACCESS_TOKENS = config['GITHUB_TOKENS'].split(',')
USER_AGENT = 'agent' 
USER_COOKIES = config['DOTCOM_USER_COOKIES'].split(',')
SESSION_COOKIES = config['USER_SESSION_COOKIES'].split(',')

KEYWORDS  = ['intents']

REPOSITORIES_FILE = 'results/02_results/repositories_commit.csv'
RESULTS_FOLDER = 'results/03_results'
CHATBOTS_FILE = 'chatbot_repositories.csv'
NOT_CHATBOTS_FILE = 'not_chatbot_repositories.csv'
NOT_INDEXED_REPO_FILE = 'not_indexed_repositories.csv'
NOT_FOUND_REPOSITORIES_FILE = 'not_found_repositories.csv'
CSV_SEPARATOR= ';'



def search_keywords_in_repo(keywords, repo_full_name, token, page):
    headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': USER_AGENT
    }
    
    delimiter = " "
    query = delimiter.join(keywords)
    #search_url = f"{GITHUB_API_URL}/search/code?q={query}+in:file+extension:yml+OR+extension:yaml+repo:{repo_full_name}"
    search_url = f"{GITHUB_API_URL}/search/code?q={query}+in:file+extension:yml+repo:{repo_full_name}&page={page}&per_page=100"
    #print(search_url)

    retries = 0

    response = requests.get(search_url, headers=headers)

    while retries < 5 and (response.status_code == 403 or response.status_code == 429):
        sleep(response)
        response = requests.get(search_url, headers=headers)
        retries = retries+1

    return response



def check_repositories(repositories, t_index):
    print(ACCESS_TOKENS[t_index])

    headers = ['full-name','html-url', 'stars','forks','created-at','updated-at','pushed-at','default-branch','owner-name','owner-id','owner-type', 'is-fork', 'fork-parent', 'last-commit', 'last-commit-date', 'domain-files', 'n-domain-files']

    cb_file = open(RESULTS_FOLDER + '/' + str(t_index)+'_'+CHATBOTS_FILE, 'w', newline='')
    chatbots = csv.DictWriter(cb_file, fieldnames=headers, delimiter=CSV_SEPARATOR)
    chatbots.writeheader()

    ncb_file = open(RESULTS_FOLDER + '/' + str(t_index)+'_'+NOT_CHATBOTS_FILE, 'w', newline='')
    not_chatbots = csv.DictWriter(ncb_file, fieldnames=headers[:-1], delimiter=CSV_SEPARATOR)
    not_chatbots.writeheader()

    ni_repo_file = open(RESULTS_FOLDER + '/' + str(t_index)+'_'+NOT_INDEXED_REPO_FILE, 'w', newline='')
    ni_repo = csv.DictWriter(ni_repo_file, fieldnames=headers[:-1], delimiter=CSV_SEPARATOR)
    ni_repo.writeheader()
    
    for repo in repositories:

        page = 1
        check_response = search_keywords_in_repo(KEYWORDS, repo['full-name'], ACCESS_TOKENS[t_index], page)
        if check_response.status_code == 404:
            if not os.path.isfile(NOT_FOUND_REPOSITORIES_FILE):
                not_found_repo_file = open(NOT_FOUND_REPOSITORIES_FILE, 'w', newline='')
                not_found_csv = csv.DictWriter(not_found_repo_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)
                not_found_csv.writeheader()
            else:
                not_found_repo_file = open(NOT_FOUND_REPOSITORIES_FILE, 'a', newline='')
                not_found_csv = csv.DictWriter(not_found_repo_file, fieldnames=reader.fieldnames, delimiter=CSV_SEPARATOR)

            not_found_csv.writerow(repo)
            not_found_repo_file.close()
            print(f"Error 404 for repository {repo['full-name']}")
            break
        print(check_response)
        
        if check_response.status_code == 403 or check_response.status_code == 429:
            print('Too many retries')
            sys.exit()

            
        if check_response.status_code != 200:
            print(f"Error in repository check: {check_response.status_code}")
            print(check_response.content)
            sys.exit()
        else:
            check_result = check_response.json()

        if check_result['total_count'] == 0:
            if is_indexed(t_index, repo['full-name']):
                print(f"Repository {repo['full-name']}: Not a chatbot")
                not_chatbots.writerow(repo)
            else:
                print(f"Repository {repo['full-name']}: Not indexed yet")
                ni_repo.writerow(repo)
        else:
            print(f"Repository {repo['full-name']}: Chatbot")
            domain_files = []
            found_all = False
            repo['n-domain-files'] = check_result['total_count'] 

            while not found_all:
                for f in check_result['items']:
                    domain_files.append(f['path'])
                if check_result['total_count'] > len(domain_files):
                    page += 1
                    check_response = search_keywords_in_repo(KEYWORDS, repo['full-name'], ACCESS_TOKENS[t_index], page)
                    if check_response.status_code == 403 or check_response.status_code == 429:
                        print('Too many retries')
                        sys.exit()

                    if check_response.status_code != 200:
                        print(f"Error in repository check: {check_response.status_code}")
                        print(check_response.content)
                        sys.exit()
                    else:
                        check_result = check_response.json()
                else:
                    found_all = True
        
            repo['domain-files'] = domain_files
            chatbots.writerow(repo)
        
        remaining = int(check_response.headers['X-RateLimit-Remaining'])

        if remaining <= 1: # github api error, should be 0
            cb_file.flush()
            ncb_file.flush()
            ni_repo_file.flush()
            sleep(check_response)
            
    
    cb_file.close()
    ncb_file.close()
    ni_repo_file.close()


def sleep(response):
    try:
        sleep_seconds = int(response.headers['X-RateLimit-Reset']) - time.time() + 2
    except:
        sleep_seconds = 60
    if sleep_seconds <= 0:
        sleep_seconds = 60
    
    print(f'Primary rate limit exceeded. Waiting for {sleep_seconds}s...')
    time.sleep(sleep_seconds)
    print('Rate limit reset. Continuing...')



def is_indexed(t_index, repo_name):

    url = 'https://github.com/search?q=repo:'+repo_name+' intents&type=code'
    session = requests.Session()

    cookies = {
        'user_session': SESSION_COOKIES[t_index],
        'dotcom_user': USER_COOKIES[t_index],
        'logged_in': 'true',
    }

    session.cookies.update(cookies)

    response = session.get(url)

    retries = 0
    while retries < 5 and (response.status_code == 403 or response.status_code == 429):
        sleep(response)
        response = session.get(url)
        retries = retries+1

    if retries == 5:
        print('Too many retries')
        sys.exit()

    if response.status_code == 200:

        if "This repository's code is being indexed right now. Try again in a few minutes" in response.text or "This repository's code has not been indexed yet. Try again later." in response.text:
            return False
        else:
            return True
        

if not os.path.isdir(RESULTS_FOLDER):
    os.mkdir(RESULTS_FOLDER)
    
repo_file = open(REPOSITORIES_FILE, 'r')
reader = csv.DictReader(repo_file, delimiter=CSV_SEPARATOR)
repos = list(reader)

t1 = threading.Thread(target=check_repositories, args=(repos[0:10], 0)) 
t2 = threading.Thread(target=check_repositories, args=(repos[10:20], 1)) 
t3 = threading.Thread(target=check_repositories, args=(repos[20:30], 2))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

repo_file.close()
