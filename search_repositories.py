import requests

from dotenv import dotenv_values
from datetime import datetime


config = dotenv_values('config.env')


GITHUB_API_URL = "https://api.github.com"
ACCESS_TOKEN = config['GITHUB_TOKEN']
USER_AGENT = 'agent' 


REPO_KEYWORDS = ['rasa', 'chatbot'] 
RESULT_FILE = 'repositories.csv'
CSV_SEPARATOR= ';'
  

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': USER_AGENT
}

# Search repositories with keywords
def execute_query(keywords, page, dt):
    delimiter = "+"
    query = delimiter.join(keywords)
    print("Searching repositories")
    search_url = f"{GITHUB_API_URL}/search/repositories?q={query}+in:name,description,topics,readme+pushed:<{dt.isoformat()}&sort=updated&page={page}&per_page=100"
    print(search_url)
    repo_response = requests.get(search_url, headers=headers)
    return repo_response


def search_repositories():
    repo_file = open(RESULT_FILE, 'w')
    repo_file.write('full-name'+CSV_SEPARATOR+'html-url'+CSV_SEPARATOR+'stars'+CSV_SEPARATOR+'forks'+CSV_SEPARATOR+'created-at'+CSV_SEPARATOR+'updated-at'+CSV_SEPARATOR+'pushed-at'+CSV_SEPARATOR+'owner-name'+CSV_SEPARATOR+'owner-id'+CSV_SEPARATOR+'owner-type\n')
    page = 1
    list_completed = False
    dt = datetime.today()
    min_pushed_date = dt

    while not list_completed:

        repo_response =  execute_query(REPO_KEYWORDS, page, dt)

        if repo_response.status_code != 200:
            print(f"Error in search: {repo_response.status_code}")
            break

        repositories = repo_response.json()
        if page==1:
            print(f"Total repositories: {repositories['total_count']}")
        print(f'Checking page {page}')

        if repositories is None or 'items' not in repositories:
            print("No repository found - Error in repository search")
            break

        for repo in repositories['items']:
            repo_file.write(repo['full_name']+CSV_SEPARATOR+repo['html_url']+CSV_SEPARATOR+str(repo['stargazers_count'])+CSV_SEPARATOR+str(repo['forks_count'])+CSV_SEPARATOR
                        + repo['created_at'] + CSV_SEPARATOR + repo['updated_at'] + CSV_SEPARATOR + repo['pushed_at'] + CSV_SEPARATOR
                        + repo['owner']['login']+CSV_SEPARATOR+str(repo['owner']['id'])+CSV_SEPARATOR+repo['owner']['type']+'\n')
            
            if min_pushed_date > datetime.fromisoformat(repo['pushed_at'].rstrip('Z')):
                min_pushed_date = datetime.fromisoformat(repo['pushed_at'].rstrip('Z'))

        if page == 10:
            page = 1
            dt = min_pushed_date
        else:
            if 'next' in repo_response.links:
                page += 1
            else:
                list_completed = True

    repo_file.close()


search_repositories()
