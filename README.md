# From the TOFU-R Snapshot to the BRASATO Curated Dataset

This repository contains all materials related to the work *"Towards the Assessment of Task-based Chatbots: From the TOFU-R Snapshot to the BRASATO Curated Dataset"*. Specifically, it includes:
- The **TOFU-R dataset**, consisting of Rasa open-source chatbots collected from GitHub.
- The **BRASATO dataset**, a curated subset of selected chatbots derived from TOFU-R.
- The **methodology scripts** used to create both datasets.
- The **analysis of ChatGPT parameters** for the extraction of external services.


The datasets are updated to **14/01/2025**.

## Information
**Target Badge**: Reproducible Badge

**Paper Title**: Towards the Assessment of Task-based Chatbots: From the TOFU-R Snapshot to the BRASATO Curated Dataset

**Submission Number**: 90

**Authors**: Elena Masserini, Diego Clerissi, Daniela Micucci, João R. Campos, Leonardo Mariani

**Contacts**: elena.masserini@unimib.it


## Artifact Description
This repository has the following structure:
- **Methodology scripts**: all scripts necessary to replicate the procedure step-by-step are numbered and their use is described in the following sections.
- **Original result folders**: intermediate results of each step generated in the original execution are stored in the *original_results* folder, organized by step number.
- **ChatGPT parameter analysis**: all materials related to the analysis of ChatGPT parameters for services extraction are available in *chatGPT_parameter_analysis* folder, along with a dedicated README.
- **Datasets**:  the TOFU-R and BRASATO datasets, which are the outputs of steps 14 and 18 respectively, are also provided directly in the main folder for convenience (file *TOFU-R.csv* and file *BRASATO.CSV*).

The following sections describe each step in detail, allowing for full replication of the procedure used to create the TOFU-R and BRASATO datasets.


## Expected Behaviour
The TOFU-R and BRASATO datasets are the results of the methodology illustrated in the paper *"Towards the Assessment of Task-based Chatbots: From the TOFU-R Snapshot to the BRASATO Curated Dataset"*. This methodology is implemented as a sequence of 18 Python scripts: the TOFU-R dataset is the result of the 14th step, while BRASATO is the final result of the last script. 

Each step produces an intermediate result, saved in folder *results*. The expected behaviour of each script and the intermediate output of each step is explained in sections *TOFU-R: a snapshot of GitHub Rasa chatbots* and *BRASATO: a curated selection*


## Environment Setup
The methodology scripts were executed with Python 3.10.11, on these two machines:

### Machine1
**Type**: Physical machine  
**OS**: Windows 11  
**CPU**: 13th Gen Intel(R) Core(TM) i7-1355U (1.70 GHz)  
**RAM**: 16 GB  

### Machine2
**Type**: Virtual Machine (Azure)  
**OS**: Linux Ubuntu  
**CPU**: 4 virtual CPUs  
**RAM**: 14 GiB  

As far as we know, the scripts do not require specific RAM and CPU to run. Some steps that involve the download or the analysis of repository zip archives may require more time on less performing machines, but to mitigate this problem the number of repositories / chatbots considered for each step can be configured. 

### Configuration
Create a config.env file from the template config.env.sample and complete it as explained below:

- **GITHUB_TOKEN**: GitHub fine-grained personal access token with *Read-only access to public repositories* as *Repository access* (required for steps 1, 2). 

- **DETECT_LANGUAGE_KEY**: API key for the [Detect Language API](https://detectlanguage.com/) (required for steps 11, 12). The API has a free plan. 

- **LLM**: Large Language Model (LLM) API to use (required for steps 16 and 18). Accepted values:
    - `OPENAI`: [Azure OpenAI API](https://azure.microsoft.com/en-us/products/ai-services/openai-service). It does not offer a free tier and requires the deployment of a gpt model in your Azure subscription. 
    - `GEMINI`: [Google Gemini API](https://ai.google.dev/gemini-api/docs). The API has a free plan. 

- **LLM_KEY**: API key for the LLM API.

- **LLM_ENDPOINT**: endpoint of the model to be used.
    - *Azure OpenAI*: the endpoint of your own model.
    - *Google Gemini*: the endpoint of a given model. Suggested: https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent

> The original experimentation was based on Azure OpenAI using the GPT-4o model. However, to make the procedure accessible without requiring a paid subscription or an Azure account, we also added support for Google Gemini, which offers a free usage tier. With Google Gemini the results may vary from the original ones since it is a different model and, unlike GPT4o, it uses default temperature and top_p values.

### Setup
You can set up the environment using a Docker environment or a Python virtual enviroment.

**Docker environment**
1. Build the docker image: 
    ```
    docker build -t rasa-dataset . 
    ```
2. Run a docker container with this image: 
    ```
    docker run --rm -it -v "${PWD}/results:/app/results" -v "${PWD}/chatbot_repositories_zip:/app/chatbot_repositories_zip" rasa-dataset
    ```


**Python virtual environment**
1. Download Python [3.10.11](https://www.python.org/downloads/release/python-31011/) 
2.  Install Python 3.10.11 (not required for Windows)
3.  Create a [Python virtual enviroment](https://docs.python.org/3/library/venv.html) with Python 3.10.11.
    - Windows (3.10.11 installed): 
    ```
    python -m venv <path_to_new_venv>
    ```
    - Windows (3.10.11 not installed): 
    ```
    <path_to_python3.10.11.exe> -m venv <path_to_new_venv>`
    - Linux/MacOS: `python3 -m venv <path_to_new_venv>
    ```
4. Activate the virtual environment:
    - Windows: 
    ```
    <path_to_new_venv>\Scripts\activate
    ```
    - Linux/MacOS: 
    ```
    source <path_to_new_venv>/bin/activate
    ```
5. Install the required python libraries included in the requirements file: 
    ```
    pip install requirements.txt
    ```


## Getting Started

### The TOFU-R and BRASATO methodology
All the methodology steps are described in the following section, along with their output and parameters. To get started with the methodology, execute it on small set of repositories, specifically:

- **Step 1**: 500 repositories
- **Step 2**: 250 repositories
- **Step 3**: 250 repositories, 7 seconds timeout
- **Step** 4-18: on the remaining ones

This execution should take around 30 minutes, but you can also reduce the considered sample at any time in the procedure.

Note that the original experimentation is based on the 8634 repositories collected and downloaded on the **14/01/2025**. A new execution of the scripts will not generate the same output, since the set of available repositories on GitHub has changed from January.

> After the procedure section you can find the reproducibility one, with all the instruction to partially reproduce the original results.


## TOFU-R: a snapshot of GitHub Rasa chatbots

### 1. Repository search
Search for GitHub repositories containing the keywords 'Rasa' and 'Chatbot' in the README, title, topics, or description.  

**Paper corresponding step**: Creation of the TOFU-R dataset - Repository Search

**Output**:   
- `repositories_json`: folder with the complete JSON responses for all retrieved repositories
- `repositories.csv`: repository dataset of all the parsed repositories

**Optional parameters**: 

- `--n-repos <n>`: maximum number of repositories to retrieve. Must be a multiple of 100, as the GitHub API returns up to 100 results per request. (default: all available results)

```
python 01_search_repositories.py [--n-repos <n>]
```

### 2. Last commit retrieval
Retrieve the sha and date of the last commit on the default branch for each repository to keep a reference to a same repository version.

**Paper corresponding step**: Creation of the TOFU-R dataset - Repository Search

**Output**: 
- `repositories_commit.csv`: repository dataset enriched with the last commit.
- `empty_repositoriescsv`: repositories with no commits.

**Optional parameters**: 
- `--n-repos <n>`: number of repositories to consider (default: all)

```
python 02_find_commit.py [--n-repos <n>]
```

### 3. Repository classification
Classify repositories as *chatbot_repositories* and *non_chatbot_repositories* based on the presence of a Rasa domain file in the repository.

**Paper corresponding step**: Creation of the TOFU-R dataset - Repository Classification

**Output**:
- `chatbot_repositories_zip`: folder with he zip archives of all chatbot repositories.
- `chatbot_repositories.csv`: repositories with one or more chatbots; in this cases, domain files found by the API are saved in field *domain-files*.
- `not_chatbot_repositories.csv`: repositories without chatbots.
- `not_found_repositories.csv`: repositories no longer available on GitHub.
- `timeout_repositories.csv`: repositories which zip archive could not be downloaded within the chosen timeout.

 > If you wish to periodically synchronize folder *chatbot_repositories_zip* with Google Drive, install [rclone](https://rclone.org/), configure a remote named gdrive, and uncomment all sync() lines.

**Optional parameters**: 
- `--n-repos <n>`: number of repositories to consider (default: all)
- `--timeout <t>`: timeout (s) for the zip archive download  (default: no timeout)

```
python 03_check_repositories.py [--n-repos <n> --timeout <t>]
```

### 4. Domain files filtering
Remove invalid domain files (empty files, non-parsable files or incorreclt identified).

**Paper corresponding step**: Creation of the TOFU-R dataset - Chatbot Extraction

**Output**: 
- `chatbot_repositories.csv`: updated chatbot repository dataset.
- `discarded_repositories.csv`: repositories with no domain file left after the filtering
- `clean_domain_statistics.txt`: statistics about the filtering process

**Optional parameters**: 
- `--n-repos <n>`: number of chatbots repositories to consider (default: all)

```
python 04_check_domain_files.py [--n-repos <n>]
```

### 5. NLU, actions and README files extraction
Enrich the dataset with information about NLU files / folder, actions files / folders and README files.

**Paper corresponding step**: Creation of the TOFU-R dataset - Chatbot Extraction

**Output**:
- `chatbot_repositories_files.csv`: chatbot repository dataset enriched with information about files.

**Optional parameters**: 
- `--n-repos <n>`: number of chatbots repositories to consider (default: all)

```
python 05_find_files.py [--n-repos <n>]
```

### 6. Chatbot identification
Identify chatbots in chatbot repositories based on the organization of their domain files (one chatbot for each folder, called *domain-folder*, that contains at least one domain file). Chatbots are classified as:
- **SFSD**: chatbot identified in a single domain-folder repository, that has a single domain file.
- **SFMD**: chatbot identified in a single domain-folder repository, that has multiple domain files.
- **MFSD**: chatbot identified in a multi domain-folder repository, that has a single domain file.
- **MFMD**: chatbot identified in a multi domain-folder repository, that has multiple domain files.

**Paper corresponding step**: Creation of the TOFU-R dataset - Chatbot Extraction

**Output**: 
- `chatbots_sfsd.csv`: SFSD chatbots.
- `chatbots_sfmd.csv`: SFMD chatbots.
- `chatbots_mfsd.csv`: MFSD chatbots.
- `chatbots_mfmd.csv`: MFMD chatbots. 

```
python 06_classify_chatbot_repositories.py
```

### 7. Domain parameter extraction
Extract domain parameters (e.g., intents, entities, slots, version) from domain files.

**Paper corresponding step**: Creation of the TOFU-R dataset - Parameter Extraction

**Output**:
- `chatbots_sfsd_info.csv`: SFSD chatbots enriched with domain parameters, one row per each domain file.
- `chatbots_sfmd_info.csv`: SFMD chatbots enriched with domain parameters, one row per each domain file.
- `chatbots_mfsd_info.csv`: MFSD chatbots enriched with domain parameters, one row per each domain file.
- `chatbots_mfmd_info.csv`: MFMD chatbots enriched with domain parameters, one row per each domain file.
- `chatbots_errors.csv`: domain files with semantically incorrect structure that reaised exceptions.

**Optional parameters**:
- `--n-sfsd <n>`: number of SFSD chatbots to consider (default: all)
- `--n-sfmd <n>`: number of SFMD chatbots to consider (default: all)
- `--n-mfsd <n>`: number of MFSD chatbots to consider (default: all)
- `--n-mfmd <n>`: number of MFMD chatbots to consider (default: all)

```
python 07_analyze_domain.py [--n-sfsd <n>] [--n-sfmd <n>] [--n-mfsd <n>] [--n-mfmd <n>] 
```

### 8. Multi-domain chatbots handling
Handle multi-domain (MD) chatbots by classifying them as:
- **Copy domain**: multiple domain files are copies, only one is kept.
- **Modularized domain**: chatbot's domain has been modularized into many domain files with no intersection between them. A unified version of their parameters is saved.
- **Discarded**: chatbots with domain files that are neither copies nor a modularized domain are discarded.

**Paper corresponding step**: Creation of the TOFU-R dataset - Parameter Extraction

**Output**:
- `chatbots_sfmd_info.csv`: SFMD chatbots classified and solved.
- `chatbots_mfmd_info.csv`: MFMD chatbots classified and solved.

**Optional parameters**:
- `--n-sfmd <n>`: number of SFMD chatbots to consider (default: all)
- `--n-mfmd <n>`: number of MFMD chatbots to consider (default: all)

```
python 08_handle_multi_domain.py [--n-sfmd <n>] [--n-mfmd <n>] 
```

### 9. Chatbot files unification
Create a unified dataset with all chatbots of different classes.

**Paper corresponding step**: Creation of the TOFU-R dataset - Parameter Extraction

**Output**:
- - `chatbots.csv`: complete dataset of chatbots extracted from the collected repositories.

```
python 09_unify_chatbot_dataset.py
```

### 10. Configuration language extraction
Extract the model configuration language from configuration files.

**Paper corresponding step**: Creation of the TOFU-R dataset - Language Extraction

**Output**:
- `chatbots_join_config_file.csv`: chatbot dataset enriched with config file information.
- `chatbots.csv`: chatbot dataset enriched with configuration language.

**Optional parameters**:
- `--n-chatbots <n>`: number of chatbots to consider (default: all)

```
python 10_extract_config_language.py [--n-chatbots <n>]
```

### 11. Training language extraction
Extract the language used in training phrases via [detectlanguage](https://detectlanguage.com/) API.

**Paper corresponding step**: Creation of the TOFU-R dataset - Language Extraction

**Output**:
- `chatbots_join_nlu_file.csv`: chatbot dataset enriched with nlu file information.
- `chatbots.csv`: chatbot dataset enriched with training language.

**Optional parameters**:
- `--n-chatbots <n>`: number of chatbots to consider (default: all)

```
python 11_extract_training_language.py [--n-chatbots <n>]
```

### 12. Response language extraction
Extract the language used in response phrases via [detectlanguage](https://detectlanguage.com/) API.

**Paper corresponding step**: Creation of the TOFU-R dataset - Language Extraction

**Output**:
- `chatbots.csv`: chatbot dataset enriched with response language.

**Optional parameters**:
- `--n-chatbots <n>`: number of chatbots to consider (default: all)

```
python 12_extract_response_language.py [--n-chatbots <n>]
```

### 13. Language evaluation

**A. Overall language evaluation**  
Identify the overall languages of a chatbot.

**Output**:
- `chatbots_language_check.csv`: chatbot dataset enriched with overall language and information about the use of English.

```
python 13_evaluate_language.py
```

**B. Manual check on multiple languages (optional)**  
Since Detect Language API may identify more languages incorrectly, perform a manual check over chatbots with more than one language to remove - correct them. 

**Paper corresponding step**: Creation of the TOFU-R dataset - Language Extraction

**Output**: 
-  `chatbots.csv`: copy file `chatbots_language_check.csv`and rename it `chatbots.csv`. Perform your manual changes in this file.

> If you want to skip step 13-B, just copy file `chatbots_language_check.csv` and rename it `chatbots.csv`, since step 14 requires as input a `chatbots.csv` file under folder *results/13_results*. 



### 14. Duplicate chatbots removal
Remove multiple copies of the same chatbot from the dataset, keeping only the best one based on these criteria: Rasa version, number of stars, number of forks and creation date.

**Paper corresponding step**: Creation of the TOFU-R dataset - Duplicate Removal

**Output**:
- `chatbots_join_nlu_date.csv`: chatbot dataset enriched with dates information.
- `copies.csv`: all copies identified in the dataset.
- `copies_to_keep`: the best chatbots for each copy group.
- `chatbots.csv`: chatbot dataset with no more copies -> the TOFU-R dataset.

**Optional parameters**:
- `--n-chatbots <n>`: number of chatbots to consider (default: all)

```
python 14_delete_duplicate_chatbots.py [--n-chatbots <n>]
```

## BRASATO: a curated selection

### 15. Chatbot selection
Select from the TOFU-R dataset a subset of chatbots with criteria based on dialogue complexity, functional complexity and usability.

**Paper corresponding step**: Creation of the BRASATO dataset - Chatbot Selection

**Output**:
- `chatbots.csv`: chatbot dataset of selected subjects.

```
python 15_select_chatbots.py
```

### 16. External service extraction
Automatically extract the external services used by the chatbot from the README and action files with an LLM (OpenAI GPT or Google Gemini).

**Paper corresponding step**: Creation of the BRASATO dataset - External Service Extraction

**Output**:
- `chatbots_join_files.csv`: chatbot dataset enriched with readme and action files information.
- `chatbots.csv`: chatbot dataset enriched with external services.
- `chatgpt_responses`: a folder with all merges requests and responses for each chatbot.

**Optional parameters**:
- `--n-chatbots <n>`: number of chatbots to consider (default: all)

```
python 16_extract_external_services.py [--n-chatbots <n>]
```

### 17. External services filtering
Filter external services incorrectly identified.

**Paper corresponding step**: Creation of the BRASATO dataset - External Service Extraction

**A. Automatic filtering**: remove services that match the *black-list* (common python local framework and libraries).
**Output**: 
-  `1_chatbots.csv`: chatbot dataset with automatically filtered services.

```
python 17_filter_external_services.py
```

**B. Manual filtering**: check the resulting file to:
- Remove values that are not external services (e.g., script names, repeated services)
- Remove non-working services (deprecated APIs)
- Remove non-used services (services that do not appear within the code or the readme)
- Normalize services names across chatbots (e.g., mysql, mysql-connector, MySQL)
- Normalize database and endpoint names (e.g., "JSON files" instead of "file1.json", or "Local server" instead of localhost endpoints").

**Output**: 
-  `2_chatbots.csv`: save the filtered chatbot dataset in this file.

**C. Services merge**: merge services extracted from action files and readme files into a single field called *external-services*.

**Output**: 
-  `3_chatbots.csv`: save the resulting chatbot dataset in this file.


### 18. Topic classification
Determine the topic of each chatbot with an LLM (OpenAI GPT or Google Gemini), based on the Google Play categories list.

**Paper corresponding step**: Creation of the BRASATO dataset - Topic Extraction

**Output**:
- `chatbots_join_readme.csv`: chatbot dataset enriched with readme files information.
- `chatgpt_responses`: a folder with all requests and responses for each chatbot.
- `chatbots.csv`: chatbot dataset enriched with topic -> the BRASATO dataset.

**Optional parameters**:
- `--n-chatbots <n>`: number of chatbots to consider (default: all)

```
python 18_extract_topic.py [--n-chatbots <n>]
```


## Reproducibility: TOFU-R and BRASATO
This section explains how to reproduce the results of the original experimentation presented in "Towards the Assessment of Task-based Chatbots: From the TOFU-R Snapshot to the BRASATO Curated Dataset".

### Reproducibility warnings

**Different state of repositories**  
The output of some steps depend on the current state of GitHub repositories, so results may still differ from the original ones. To limit this problem, the reproduction process can start with step 3, as explained in the following section *How to reproduce the original results*.

**Four hours limitation**  
The complete execution of all scripts requires more than 4 hours, expecially the zip archives download (step 3). To overcome this problem, every step can be executed of a subset of the available repositories: optional parameters specific for each script define the number of repositories / chatbots that will be considered in the execution.

**API limitations**
The APIs used in this project have the following limits:
- **GitHub API** (step 1, 2): 5000 requests/hour. 
- **DetectLanguageAPI** (step 11, 12): 1000 requests/day, 1 MB/day.
- **Google Gemini API** (step 16, 18): 100/1000 requests/day, 5/30 requests/minute [depending on the model](https://ai.google.dev/gemini-api/docs/rate-limits)

The complete execution on all repositories / chatbots overcomes this limits.

**Zip files space on disk**  
From step 3 zip archives of chatbots repositories will be download and saved on disk for the following steps. The size of the complete set of zip archives in the original execution is 150 GB. 

### How to reproduce the original results
The intermediate original results of each step are available in folder *original_results*, so that results can be compared step by step.

To partially replicate the original procedure you can use the original results of step 2 as a base for the execution of the following steps. Steps 1, 2 and 3 in fact depend on the current state of GitHub repositories, specifically:

- **Step 1**: new repositories with terms *Rasa* and *Chatbot* have been added from January, and some of the ones identified in January have been deleted or updated, so the generated list or repositories is different in size and content.

- **Step 2**: even when executed starting from the original list of repositories collected in January, the output will be different because many repositories have been updated with new commits.

- **Step 3**: even when executed starting from the original result of step 2, some repositories may no longer be available and they will fall under *not found*. When setting a timeout (it is the suggested choice, since some zip archives are heavy and require many minutes), some repositories will fall under *timeout*, differently from the original execution that had no timeout but required many many hours. 

To limit this dependance on GitHub, start the replication process by executing step 3 on the original results of step 2. Step 3 is also dependant on GitHub state but in a less heavy way, and its execution cannot be skipped in the reproduction process by starting direclty with step 4, because step 3 involves the download of zip archives required for the following steps, and we cannot legally include the original zip archives in this repository nor distribute them in other ways. Differences in step 3 results (chatbot repositories becoming not found repositories, timeout repositories) will propagate to the rest of the results.

Given the space/time/API limitations involved in the execution of the procedure on the complete set of repositories, the suggested choice is to reproduce the procedure on a subset of the original repositories. You can execute step 3 with the following parameters:
- `--n-repos <n>`: 500/700
- `--timeout <t>`: 8-10 seconds

> The script execution will overwrite previuos results, so to begin the reproduction process from step 3, copy folders *01_results*, *02_results* from *original_results* to *results/* before launching script 3.


## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.