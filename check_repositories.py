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

KEYWORDS  = ['intents']

REPOSITORIES_FILE = 'repositories.csv'
CHATBOTS_FILE = 'chatbots.csv'
NOT_CHATBOTS_FILE = 'not_chatbots.csv'
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


def check_rate_limit(token):
    headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': USER_AGENT
    }
    response = requests.get('https://api.github.com/rate_limit', headers=headers)
    return response




def check_repositories(repositories, t_index):
    print(ACCESS_TOKENS[t_index])

    headers = ['full-name','html-url', 'stars','forks','created-at','updated-at','pushed-at','owner-name','owner-id','owner-type','domain-files']

    cb_file = open(str(t_index)+'_'+CHATBOTS_FILE, 'a', newline='')
    chatbots = csv.DictWriter(cb_file, fieldnames=headers, delimiter=CSV_SEPARATOR)
    #chatbots.writeheader()

    ncb_file = open(str(t_index)+'_'+NOT_CHATBOTS_FILE, 'a', newline='')
    not_chatbots = csv.DictWriter(ncb_file, fieldnames=headers[:-1], delimiter=CSV_SEPARATOR)
    #not_chatbots.writeheader()
    
    for repo in repositories:
        limit_response = check_rate_limit(ACCESS_TOKENS[t_index])

        if limit_response.status_code == 200:
            code_search_limit = limit_response.json()['resources']['code_search']
            print(code_search_limit)

            if code_search_limit['remaining'] <= 1: # github api error, should be 0
                cb_file.flush()
                ncb_file.flush()
                sleep_seconds = code_search_limit['reset'] - time.time() + 1
                print(f'Primary rate limit exceeded. Waiting for {sleep_seconds}s...')
                time.sleep(sleep_seconds)
                print('Rate limit reset. Continuing...')

            check_response = search_keywords_in_repo(KEYWORDS, repo['full-name'], ACCESS_TOKENS[t_index])
            if check_response.status_code != 200:
                print(f"Error in repository check: {check_response.status_code}")
                print(check_response.content)
                sys.exit()
            else:
                check_result = check_response.json()
            if check_result['total_count'] == 0:
                print(f"Repository {repo['full-name']}: Not a chatbot")
                not_chatbots.writerow(repo)
            else:
                print(f"Repository {repo['full-name']}: Chatbot")
                domain_files = []
                for f in check_result['items']:
                    domain_files.append(f['path'])
                
                repo['domain-files'] = domain_files
                chatbots.writerow(repo)
        else:
            print(f"Error in rate limit check: {limit_response.status_code}")
    
    
    cb_file.close()
    ncb_file.close()
        


repo_file = open(REPOSITORIES_FILE, 'r')
reader = csv.DictReader(repo_file, delimiter=CSV_SEPARATOR)
repos = list(reader)


t1 = threading.Thread(target=check_repositories, args=(repos[75:181], 0))
t2 = threading.Thread(target=check_repositories, args=(repos[255:361], 1))
t3 = threading.Thread(target=check_repositories, args=(repos[434:541], 2))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()


repo_file.close()
