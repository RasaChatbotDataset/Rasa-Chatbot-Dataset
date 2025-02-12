# Rasa Chatbot Dataset

This repository contains a dataset of Rasa open source chatbots from GitHub. The dataset is updated to 14/01/2025.

The code used to build the dataset is also available in this repository. To replicate the procedure, follow the steps in the following section.

## How to build a Rasa chatbot dataset

### 1. Configuration
Create a config.env file from the template config.env.sample and complete it as explained below:

- **GITHUB_TOKENS**: three GitHub personal access tokens from three different GitHub accounts. 

- **DOTCOM_USER_COOKIES**: three GitHub user names (of three additional GitHub accounts than those reported for the variable GITHUB_TOKENS).

- **USER_SESSION_COOKIES**: three session cookies, each for one of the GitHub accounts used in the filed *DOTCOM_USER_COOKIES*. You can open a session from the brower for each GitHub account and copy this value from Inspect -> Application -> Cookies -> https://github.com -> user_session.

- **DETECT_LANGUAGE_KEY**: API key for the [detect language API](https://detectlanguage.com/).

- **OPENAI_KEY**: API key for OpenAI personal model.

- **OPENAI_ENDPOINT**: API model endpoint.


> Using three GitHub tokens and three GitHub session cookies (six GitHub accounts) instead of one and one speeds up the chatbot-check process by allowing to multi-thread it. If you want to use only one GitHub token and one GitHub session (two GitHub accounts) you will have to modify script *check_repositories.py* with one thread instead of three and you will need to change how access tokens and session cookies are read from config file in all scripts (not an array anymore but a single variable).

### 2. Repositories search
Execute script *search_repositories.py* to search for repositories with 'Rasa' and 'Chatbot' keywords in the README, in the title, in the topics or in the description. Complete json responses will be saved in folder *repositories_2025_json*, while only the fields of interest for each repository will be saved in file *repositories.csv*.

```
python search_repositories.py
```

### 3. Save last commit
In order to keep a reference to a same repository version execute script *find_commit.py* which saves the sha and date of the last commit on the default branch for each repository. Classification and analysis will refer to this version.

```
python find_commit.py
```

### 4. Chatbot check for indexed repositories
Execute script *check_repositories.py* to check wether a repository is a chatbot or not; this classification is based on the presence of a .yml file that contains the keyword 'intents', since all Rasa chatbots require a domain file with the definition of its intents. This check is performed via GitHub search API and works only for indexed repositories. This script will produce three csv files: 
- **chatbots_2025.csv**: repositories which are chatbots; in this cases, domain files found by the API are saved in field *domain-files*.
- **not_chatbots-2025.csv**: repositories which are not chatbots.
- **not_indexed-2025.csv**: repositories which are not indexed (they cound be chatbots or not).

```
python check_repositories.py
```

### 5. Chatbots zip download
Execute script *download_chatbots.py* to download the zip archive of all chatbots identified from the previus steps. They will be saved in folder *chatbot_zip-2025*, which is periodically synchronized with an online backup folder on Google Drive with rclone. If you want to keep this feature you will need to install rclone, configure a remote named gdrive and create a folder 'chatbot_zip-2025' on your Google Drive. Otherwise you can comment all lines with *sync()* in script *download_chatbots.py* and *check_not_indexed_repositories.py*.

```
python download_chatbots.py
```

### 6. Check not indexed repositories
Execute script *check_not_indexed_repositories.py* to classify not indexed repositories as chatbots or not-chatbots. This script downloads the zip archive of the repository and classifies it as chatbot based on the presence of a domain file; if the repository is not a chatbot, its zip archive is deleted. In this step, files *chatbots-2025.csv* and *not_chatbots-2025.csv* will be updated and chatbots zip will be saved in folder *chatbot_zip-2025*.

```
python check_not_indexed_repositories.py
```

### 7. Domain files filtering
Execute script *check_domain_files.py* to remove all domain files which were previously identified but that are actually not parsable, empty or not really a rasa domain file. Repositories with no domain files left will be removed from the list of chatbots in *chatbots_2025.csv* and will be saved in file *chatbots-2025-no-more-domains.csv*; their zip files will be deleted. Statistics about domain file filtering can be found in file *clean_domain_statistics.txt*.

```
check_domain_files.py
```

### 8. NLU, actions and readmes files check
Execute script *find_files.py* to enrich the dataset file *chatbots_2025.csv* with information about nlu files / folder, actions files / folders and readmes.

```
find_files.py
```
