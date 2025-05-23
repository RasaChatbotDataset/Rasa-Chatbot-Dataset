# From the TOFU-R Snapshot to the BRASATO Curated Dataset

This repository contains all materials related to the work "Towards the Assessment of Task-based Chatbots: From the TOFU-R Snapshot to the BRASATO Curated Dataset". Specifically, it includes:
- The TOFU-R dataset, consisting of Rasa open-source chatbots collected from GitHub.
- The BRASATO dataset, a curated subset of selected chatbots derived from TOFU-R.
- The methodology used to create both datasets.
- The analysis of ChatGPT parameters for the extraction of external services.


The datasets are updated to 14/01/2025.

## Repository structure
This repository is structured in the following way:
- **Methodology scripts**: all scripts necessary to replicate the procedure step-by-step are numbered and their use is described in the following sections.
- **Result folders**: intermediate results generated by each step are stored in *results* folder, organized by step number.
- **ChatGPT parameter analysis**: all materials related to the analysis of ChatGPT parameters for services extraction are available in *chatGPT_parameter_analysis* folder, along with a dedicated README.
- **Datasets**:  the TOFU-R and BRASATO datasets, which are the outputs of steps 16 and 20 respectively, are also provided directly in the main folder for convenience.

The following sections describe each step in detail, allowing for full replication of the procedure used to create the TOFU-R and BRASATO datasets

## Prerequisites
The script were executed using Python 3.10.11 and they require the following libraries:
- requests
- python-dotenv
- PyYAML
- deepdiff
- pandas
- detectlanguage

Dependencies can be installed with the command
```
pip install -r requirements.txt
```

## TOFU-R: a snapshot of GitHub Rasa chatbots

### 0. Configuration
Create a config.env file from the template config.env.sample and complete it as explained below:

- **GITHUB_TOKENS**: three GitHub personal access tokens from three different GitHub accounts. 

- **DOTCOM_USER_COOKIES**: The usernames of three additional GitHub accounts (different from those used for GITHUB_TOKENS).

- **USER_SESSION_COOKIES**: three session cookies, one for each GitHub account listed in *DOTCOM_USER_COOKIES*. You can open a session from the browser for each GitHub account and copy this value from Inspect -> Application -> Cookies -> https://github.com -> user_session.

- **DETECT_LANGUAGE_KEY**: API key for the [Detect Language API](https://detectlanguage.com/).

- **OPENAI_KEY**: API key for an [OpenAI API](https://platform.openai.com/docs/overview).

- **OPENAI_ENDPOINT**: endpoint of the OpenAI model to be used.


> Using three GitHub tokens and three GitHub session cookies (from six GitHub accounts) speeds up the chatbot-check process  by enabling multi-threaded execution. If you prefer to use only one GitHub token and one GitHub session cookie (two GitHub accounts) you will need to 
- Modify the script *check_repositories.py* with one thread instead of three
- Update all scripts that use GitHub tokens to read access tokens and session cookies as single variables rather than arrays.

### 1. Repository search
Search for repositories containing the keywords'Rasa' and 'Chatbot' in the README, title, topics, or description. Complete json responses are saved in *results/01_results/repositories_json*, while only the fields of interest for each repository will be saved in file *repositories.csv*.

```
python 01_search_repositories.py
```

### 2. Last commit retrieval
Retrieve the sha and date of the last commit on the default branch for each repository to keep a reference to a same repository version.

```
python 02_find_commit.py
```

### 3. Indexed repository classification
Classify repositories as *chatbot_repositories* and *non_chatbot_repositories* based on the presence of a Rasa domain file in the repository (a .yml file that contains the keyword 'intents'). The domain file presence is checked via GitHub search API, which works only for indexed repositories. This step generates 4 files: 
- **chatbot_repositories.csv**: repositories with one or more chatbots; in this cases, domain files found by the API are saved in field *domain-files*.
- **not_chatbot_repositories.csv**: repositories without chatbots.
- **not_indexed_repositories.csv**: repositories which have not been indexed by GitHub (they could contain chatbots or not).
- **not_found_repositories.csv**: repositories no longer available on GitHub.

```
python 03_check_repositories.py
```

### 4. Chatbot zip download
Download ZIP archives of all chatbot repositories identified in the previous step. The zips are saved in *chatbot_repositories_zip* folder. If you wish to periodically synchronize this folder with Google Drive, install [rclone](https://rclone.org/), configure a remote named gdrive, and uncomment all sync() lines in both this script and ```05_check_not_indexed_repositories.py```.

```
python 04_download_chatbot_repositories.py
```

### 5. Non-indexed repository classification
Classify non-indexed repositories with a local code inspection, by downloading the zip archive of each repository and checking the presence of a domain file. Only zip archives of chatbot repositories are kept and added to *chatbot_repositories_zip* folder, and updated classification files are saved in step 5 results folder.

```
python 05_check_not_indexed_repositories.py
```

### 6. Domain files filtering
Remove invalid domain files (empty files, non-parsable files or incorreclt identified). Repositories with no valid domain files left will be discarded and logged in a specific file under step 6 results folder, along with the filtered list and statistics about the filtering process.

```
python 06_check_domain_files.py
```

### 7. NLU, actions and README files extraction
Enrich the dataset with information about NLU files / folder, actions files / folders and README files.

```
python 07_find_files.py
```

### 8. Chatbot repository classification
Classify chatbot repositories based on the number and organization of domain files:
- **SFSD**: single domain folder, single domain file
- **SFMD**: single domain folder, multiple domain files
- **MF**: multiple domain folders

Multi-folder (MF) repositories will be split into *sub-chatbots*, one per each domain folder. NLU, action and readme files will be associated to a sub-chatbot based on shared path length with the domain folder. Sub-chatbots are further categorized into:
- **MFSD**: sub-chatbot with one domain file
- **MFMD**: sub-chatbot with more domain files

```
python 08_classify_chatbot_repositories.py
```

### 9. Domain parameter extraction
Extract domain parameters (e.g., intents, entities, slots, version) from domain files. A file for each chatbot-repository class (SFSD, SFMD, MFSD, MFMD) will be generated in step 9 results folder. 
```
python 09_analyze_domain.py
```

### 10. Multi-domain chatbots handling
Handle Multi-domain (MD) chatbots by analyzing their domain files and classifying them as:
- **All copy domains**: multiple domain files are copies, only one is kept.
- **All distinct domains**: chatbot's domain has been modularized into many domain files with no intersection between them. A unified version of their parameters is saved.
- **Discarded**: chatbots with domain files that neither copies nor a modularized domain are discarded.

```
python 10_handle_multi_domain.py
```

### 11. Chatbot files unification
Create a unified dataset with all chatbots and their class.
```
python 11_unify_chatbot_dataset.py
```

### 12. Configuration language extraction
Extract the model configuration language from configuration files.
```
python 12_extract_config_language.py
```

### 13. Training language extraction
Extract the language used in training phrases via [detectlanguage](https://detectlanguage.com/) API.
```
python 13_extract_training_language.py
```

### 14. Response language extraction
Extract the language used in response phrases via [detectlanguage](https://detectlanguage.com/) API.
```
python 14_extract_response_language.py
```

### 15. Language evaluation
Since detectlanguage API may identify more languages incorrectly, perform a manual check over chatbots with more than one language to remove - correct them. Save the results in a file named *chatbots_language_check.csv* under folder *results/15_results*. After this check, execute script *15_evaluate_language* to evaluate chatbots languages and the use of English.
```
python 15_evaluate_language.py
```

### 16. Chatbot copies removal
Remove multiple copies of the same chatbot from the dataset, keeping only the best one based on these criteria: Rasa version, number of stars, number of forks and creation date.
```
python 16_delete_duplicate_chatbots.py
```

## BRASATO: a curated selection

### 17. Chatbot selection
Select from the TOFU-R dataset a subset of chatbots with criteria based on dialogue complexity, functional complexity and usability.
```
python 17_select_chatbots.py
```

### 18. External services extraction
Automatically extract the external services used by the chatbot from the README and action files with ChatGPT.
```
python 18_extract_external_services.py
```

### 19. External services filtering
External services need to be checked as ChatGPT may have extracted also libraries or frameworks other than external services. This check is divided into 2 steps:

1. **Automatic**: execute script *19_filter_external_services* to remove all services that match the *black-list* (common python local framework and libraries). Results will be save in file *1_chatbots.csv*
2. **Manual**: check the resulting file to:
    - Remove values that are not external services (e.g., script names, repeated services)
    - Remove non-working services (deprecated APIs)
    - Remove non-used services (services that do not appear within the code or the readme)
    - Normalize services names across chatbots (e.g., mysql, mysql-connector, MySQL)
    - Normalize database and endpoint names (e.g., "JSON files" instead of "file1.json", or "Local server" instead of localhost endpoints").

After the filtering, you can merge services extracted from action files and readme files into a single field, *external-services*, as in file *3_chatbots.csv*.

### 20. Topic classification
Determine the topic of each chatbot with ChatGPT, based on the Google Play categories list.
```
python 20_extract_topic.py
```

    