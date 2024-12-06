import requests
import threading

from dotenv import dotenv_values
import csv
import time
import sys 
config = dotenv_values('config.env')


GITHUB_API_URL = "https://api.github.com"
ACCESS_TOKENS = config['GITHUB_TOKENS'].split(',')
USER_AGENT = 'agent' 
USER_COOKIES = config['DOTCOM_USER_COOKIES'].split(',')
SESSION_COOKIES = config['USER_SESSION_COOKIES'].split(',')

KEYWORDS  = ['intents']

REPOSITORIES_FILE = 'repositories.csv'
CHATBOTS_FILE = 'chatbots.csv'
NOT_CHATBOTS_FILE = 'not_chatbots.csv'
NOT_INDEXED_REPO_FILE = 'not_indexed.csv'
CSV_SEPARATOR= ';'



def search_keywords_in_repo(keywords, repo_full_name, token):
    headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': USER_AGENT
    }
    
    delimiter = " "
    query = delimiter.join(keywords)
    #search_url = f"{GITHUB_API_URL}/search/code?q={query}+in:file+extension:yml+OR+extension:yaml+repo:{repo_full_name}"
    search_url = f"{GITHUB_API_URL}/search/code?q={query}+in:file+extension:yml+repo:{repo_full_name}"
    print(search_url)
    response = requests.get(search_url, headers=headers)
    return response



def check_repositories(repositories, t_index):
    print(ACCESS_TOKENS[t_index])

    headers = ['full-name','html-url', 'stars','forks','created-at','updated-at','pushed-at','owner-name','owner-id','owner-type','domain-files']

    cb_file = open(str(t_index)+'_'+CHATBOTS_FILE, 'w', newline='')
    chatbots = csv.DictWriter(cb_file, fieldnames=headers, delimiter=CSV_SEPARATOR)
    chatbots.writeheader()

    ncb_file = open(str(t_index)+'_'+NOT_CHATBOTS_FILE, 'w', newline='')
    not_chatbots = csv.DictWriter(ncb_file, fieldnames=headers[:-1], delimiter=CSV_SEPARATOR)
    not_chatbots.writeheader()

    ni_repo_file = open(str(t_index)+'_'+NOT_INDEXED_REPO_FILE, 'w', newline='')
    ni_repo = csv.DictWriter(ni_repo_file, fieldnames=headers[:-1], delimiter=CSV_SEPARATOR)
    ni_repo.writeheader()
    
    for repo in repositories:

        check_response = search_keywords_in_repo(KEYWORDS, repo['full-name'], ACCESS_TOKENS[t_index])
        print(check_response)
        retries = 0
        while retries < 5 and (check_response.status_code == 403 or check_response.status_code == 429):
            sleep(check_response)
            check_response = search_keywords_in_repo(KEYWORDS, repo['full-name'], ACCESS_TOKENS[t_index])
            retries = retries+1
        
        if retries == 5:
            print('Too many retries')
            sys.exit()

        retries = 0
            
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
            for f in check_result['items']:
                domain_files.append(f['path'])
            
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

        if "This repository's code is being indexed right now. Try again in a few minutes" in response.text:
            return False
        else:
            return True
        


repo_file = open(REPOSITORIES_FILE, 'r')
reader = csv.DictReader(repo_file, delimiter=CSV_SEPARATOR)
repos = list(reader)

# 1117
t1 = threading.Thread(target=check_repositories, args=(repos[1118:1280], 0))
t2 = threading.Thread(target=check_repositories, args=(repos[1280:1442], 1))
t3 = threading.Thread(target=check_repositories, args=(repos[1442:1604], 2))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()


repo_file.close()
