# Rasa Chatbot Dataset

This repository contains a dataset of Rasa open source chatbots from GitHub. The dataset is updated to 14/01/2025.

The code used to build the dataset is also available in this repository. To replicate the procedure, follow the steps in the following section.

## How to build a Rasa chatbot dataset

### 0. Configuration
Create a config.env file from the template config.env.sample and complete it as explained below:

- **GITHUB_TOKENS**: three GitHub personal access tokens from three different GitHub accounts. 

- **DOTCOM_USER_COOKIES**: three GitHub user names (of three additional GitHub accounts than those reported for the variable GITHUB_TOKENS).

- **USER_SESSION_COOKIES**: three session cookies, each for one of the GitHub accounts used in the filed *DOTCOM_USER_COOKIES*. You can open a session from the brower for each GitHub account and copy this value from Inspect -> Application -> Cookies -> https://github.com -> user_session.

- **DETECT_LANGUAGE_KEY**: API key for the [detect language API](https://detectlanguage.com/).

- **OPENAI_KEY**: API key for OpenAI personal model.

- **OPENAI_ENDPOINT**: API model endpoint.


> Using three GitHub tokens and three GitHub session cookies (six GitHub accounts) instead of one and one speeds up the chatbot-check process by allowing to multi-thread it. If you want to use only one GitHub token and one GitHub session (two GitHub accounts) you will have to modify script *check_repositories.py* with one thread instead of three and you will need to change how access tokens and session cookies are read from config file in all scripts (not an array anymore but a single variable).

### 1. Repositories search
Execute script *01_search_repositories.py* to search for repositories with 'Rasa' and 'Chatbot' keywords in the README, in the title, in the topics or in the description. Complete json responses will be saved in under 'results/01_results', in folder *repositories_json*, while only the fields of interest for each repository will be saved in file *repositories.csv*.

```
python 01_search_repositories.py
```

### 2. Save last commit
In order to keep a reference to a same repository version execute script *02_find_commit.py* which saves the sha and date of the last commit on the default branch for each repository; results are saved in folder 'results/02_results'. Classification and analysis will refer to this version.

```
python 02_find_commit.py
```

### 3. Chatbot check for indexed repositories
Execute script *03_check_repositories.py* to check wether a repository contains a chatbot or not; this classification is based on the presence of a .yml file that contains the keyword 'intents', since all Rasa chatbots require a domain file with the definition of its intents. This check is performed via GitHub search API and works only for indexed repositories. This script will save four csv files under 'results/03_results: 
- **chatbot_repositories.csv**: repositories whit one or more chatbots; in this cases, domain files found by the API are saved in field *domain-files*.
- **not_chatbot_repositories.csv**: repositories without chatbots.
- **not_indexed_repositories.csv**: repositories which have not been indexed by GitHub (they could contain chatbots or not).
- **not_found_repositories.csv**: repositories no longer available on GitHub.

```
python 03_check_repositories.py
```

### 4. Chatbots zip download
Execute script *04_download_chatbot_repositories.py* to download the zip archive of all chatbot repositories identified from the previus steps. They will be saved in folder *chatbot_repositories_zip*, which is periodically synchronized with an online backup folder on Google Drive with rclone. If you want to keep this feature you will need to install rclone, configure a remote named gdrive, create a folder 'chatbot_repositories_zip' on your Google Drive and de-comment all lines with *sync()* in script *04_download_chatbot_repositories.py* and *05_check_not_indexed_repositories.py*.

```
python 04_download_chatbot_repositories.py
```

### 5. Check not indexed repositories
Execute script *05_check_not_indexed_repositories.py* to classify not indexed repositories as chatbot or not-chatbot repositories. This script downloads the zip archive of the repository and classifies it as chatbot repository based on the presence of a domain file; if the repository doesn not contain a chatbot, its zip archive is deleted. The updated version of files *chatbot_repositories.csv*, *not_chatbot_repositories.csv* and  *not_found_repositories.csv* will be saved in folder 'results/05_results' and chatbot repositories zip will be saved in folder *chatbot_repositories_zip*.

```
python 05_check_not_indexed_repositories.py
```

### 6. Domain files filtering
Execute script *06_check_domain_files.py* to remove all domain files which were previously identified but that are actually not parsable, empty or not really a rasa domain file. Repositories with no domain files left will be discarded and their data will be moved to file *discarded_repositories*. Results will be saved in folder 'results/06_results'. The filtered list of chatbot repositories will be saved in file *chatbot_repositories.csv*. Statistics about domain file filtering can be found in file *clean_domain_statistics.txt*.

```
python 06_check_domain_files.py
```

### 7. NLU, actions and readmes files check
Execute script *07_find_files.py* to enrich the dataset file *chatbot_repositories.csv* with information about nlu files / folder, actions files / folders and readmes. Information are saved in file *chatbots_repositories_files.csv* under 'results/07_results'.

```
python 07_find_files.py
```

### 8. Chatbot repositories classification
Based on the number of domain files and domain folders, chatbot repositories will be divided into
- **SFSD**: one domain folder, one domain file
- **SFMD**: one domain folder, more domain files
- **MF**: more domain folders

Multi-folder repositories will be split into *sub-chatbots*, one for each domain folder. NLU, action and readme files will be associated to a sub-chatbot basing on the length of the common path between the file and the domain folder of the sub-chatbot. Sub-chatbots derived from MF repositories will then be divided into:
- **MFSD**: sub-chatbot with one domain file
- **MFMD**: sub-chatbot with more domain files

Execute script *08_classify_chatbot_repositories.py* to classify chatbot repositories; results will be saved in folder 'results/08_results'.
```
python 08_classify_chatbot_repositories.py
```

### 9. Analyze domain files
Execute script *09_analyze_domain.py* to extract domain definition data from all domain files. A file for each chatbot-repository class (SFSD, SFMD, MFSD, MFMD) will be generated under 'results/09_results'. 
```
python 09_analyze_domain.py
```


### 10. Handle multi-domain files chatbots
Execute script *10_handle_multi_domain.py* to remove domain file copies from MD repositories and to automatically merge domains which are divided into more files (domain files in MD chatbots which have no intersection). Results and statistics files will be generated in folder 'results/10_results'. MD chatbots automatically handled are marked as 'solved', while the rest of them (chatbots with domain files that are not the same domain but have an intersection) will be discarded.

```
python 10_handle_multi_domain.py
```

### 11. Chatbot files unification
Execute script *11_unify_chatbot_dataset* to create a unified CSV with all the chatbots and their type.
```
python 11_unify_chatbot_dataset.py
```

### 12. Configuration language extraction
Execute script *12_extract_config_language* to extract model configuration language from configuration files.
```
python 12_extract_config_language.py
```

### 13. Training language extraction
Execute script *13_extract_training_language* to extract the language of training phrases via [detectlanguage](https://detectlanguage.com/) API.
```
python 13_extract_training_language.py
```

### 14. Response language extraction
Execute script *14_extract_response_language* to extract the language of response phrases via [detectlanguage](https://detectlanguage.com/) API.
```
python 14_extract_response_language.py
```

### 15. Chatbot copies removal
Execute script *15_delete_duplicate_chatbots* to remove copies of the same chatbot from the dataset. Copies are ordered by version, stars, forks and creation date, and only the first one will be kept; copies with same structure but different action files will be kept.
```
python 15_delete_duplicate_chatbots.py
```

### 16. Chatbot selection
Execute script *16_select_chatbots* to filter the dataset by complexity and popularity criteria.
```
python 16_select_chatbots.py
```