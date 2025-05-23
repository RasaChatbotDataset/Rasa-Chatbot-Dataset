REQUEST
Problem: This is a README file from a Rasa chatbot repository # Ask-CCI Bot

This repo contains the rasa bot project: **Ask-CCI Student Assist Bot** that was originally developed as part of the course ITIS-6112-8112 and has been further expanded for course DSBA-6345. This project was further modfied for the demo at ATL Dev Con 2022

## Table of Contents

- [Project Setup](https://github.com/bhakthil/student-assist#project-setup)
- [Installing Dependencies](https://github.com/bhakthil/student-assist#installing-dependencies)
- [How to Run The Chatbot](https://github.com/bhakthil/student-assist#how-to-run-the-chatbot)
- [How to Train the Chatbot](https://github.com/bhakthil/student-assist#how-to-train-the-chatbot)
  - [NLU](https://github.com/bhakthil/student-assist#datanluyml)
  - [Stories](https://github.com/bhakthil/student-assist#datastoriesyml)
  - [Domain](https://github.com/bhakthil/student-assist#datadomainyml)
- [How to Create a Trained Model](https://github.com/bhakthil/student-assist#how-to-create-a-trained-model)
- [Running Haystack Service](https://github.com/bhakthil/student-assist#running-haystack-service)
- [Running API Tests](https://github.com/bhakthil/student-assist#running-api-tests)

## Project Setup

1. Clone this project to your local system via:

    ```bash
    git clone https://github.com/bhakthil/student-assist.git
    ```

2. Change to the new directory:

    ```bash
    cd student-assist
    ```

3. Create a new virtual environment:

    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment

    ```bash
    source .venv/bin/activate
    ```

## Installing Dependencies

1. Update pip to the latest version

   ```bash
   pip install -U pip
   ```

2. Install `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```
    **NOTE:** If you encounter any errors please run the command again.

3. Install Docker
    - Please check Docker site for most recent installation instructions: https://docs.docker.com/desktop/

---

## How to Train The Chatbot

In order for the bot to understand different intents, it needs to be trained with sample utterances for each new intent.

There are few places that needs to be changed for a new intent to be added to the system.

## ./data/nlu.yml

Please add at least ten sample utterances for each of the intent you are responsible for. For an example, below markup is used to define `thank_you` intent.

  ```yml
  - intent: thank_you
    examples: |
    - Thanks
    - Thank You
    - thanks
    - thanks a lot
    - thank you so much
  ```

## ./data/stories.yml

Each intent should have at least 2 paths; **happy path** **and unhappy path**. So, please use below example to create paths for your intents.

```yml
- story: phd info happy path
  steps:
  - intent: phd_info
  - action: utter_phd_info
  - action: utter_did_that_help
  - intent: affirm
  - action: utter_happy
  - action: utter_continue

- story: phd info unhappy path
  steps:
  - intent: phd_info
  - action: utter_phd_info
  - action: utter_did_that_help
  - intent: deny
  - action: utter_helpdesk
  .
  .
  .
- story: **YOU_WILL_APPEND_YOUR_STORIES_HERE**
  steps:
  - intent: [new intent]
  - action: [new action]
  - action: ...
```

## ./domain.yml

Domain file is where you define the responses for each intent. You will add responses for each of your intent under `responses` section.

each response corrosponding to you utterance should be named in the format `utter_xxxx` where xxxx is the intent name that the respnse corrosponds to.

For example, the response corrosponding to `phd_info` intent is named as `utter_phd_info`.

```yml
responses:
  utter_phd_info:
  - text: "You can get more information about our PhD program at <a href='https://bit.ly/3whwJFL'>Link</a>"

  utter_msc_info:
  - text: "You can get more information about our MSc program at <a href='https://bit.ly/3GMPPIV'>Link</a>"
  .
  .
  .
  .
  utter_<YOUR_NEW_UTTERANCE >:
  - text: "YOUR NEW RESPONSE"

```

In addition, you will add your intent names under the `intents` section of the domain file.

```yml
intents:
  - greet
  - goodbye
  - affirm
  - deny
  - mood_great
  - mood_unhappy
  - bot_challenge
  - thank_you
###################
  - phd_info
  - msc_info
  - **YOU_WILL_APPEND_YOUR_INTENT(S)**
```

#### Training the Model

Once you finish adding the intents and the strories, you will be able to integrate the new additions/edits to your bot by re-training the bot.

Use below command to re-train the model:

```bash
rasa train
```

#### Testing the Model

Once you finish training your bot, you can perform a quick test by running the bot in interactive mode.

Use below command to start the bot in ineractive mode:

```bash
rasa shell --debug
```
![image](https://user-images.githubusercontent.com/12928110/165818077-81a72ed8-23ef-445c-8f07-6649b76fd03f.png)

---
## How to Run The Chatbot


### One-line operation

1. To launch all services from one script, run the following:

    ```bash
    . ./run.sh
    ```

  To run each part of the system indiviually, use the following set(s) of instructions

### Starting separate services at a time

1. First, you must start the Rasa action server:
  
   ```bash
   rasa run actions
   ```

   - If the action server is running, you should be able to see the below message:

        ```bash
      (.venv) ➜  student-assist git:(dev) ✗ rasa run actions
      2022-03-09 14:41:23 INFO     rasa_sdk.endpoint  - Starting action endpoint server...
      2022-03-09 14:41:23 INFO     rasa_sdk.executor  - Registered function for 'action_info_retrieval'.
      2022-03-09 14:41:23 INFO     rasa_sdk.executor  - Registered function for 'action_default_ask_affirmation'.
      2022-03-09 14:41:23 INFO     rasa_sdk.endpoint  - Action endpoint is up and running on http://0.0.0.0:5055
      ```

2. In a separate terminal, you can start the chatbot server by executing:
  
    ```bash
    rasa run -m models --enable-api --cors "*"
    ```

   - If the server is up and running, you should be able to see the below message:

     ```bash
     (.venv) ➜  student-assist git:(dev) ✗ rasa run -m models --enable-api --cors "*"
     2022-03-09 14:34:53 INFO     root  - Starting Rasa server on http://0.0.0.0:5005
     2022-03-09 14:34:54 INFO     rasa.core.processor  - Loading model models/20220309-143217-broad-valid.tar.gz...
     2022-03-09 14:35:31 INFO     root  - Rasa server is up and running.
     ```

When you open the [AskCCI.html](https://github.com/bhakthil/student-assist/blob/main/Chatbot-Widget/AskCCI.html) file, you will notice chat icon in the bottom-right corner

![bot icon](bot-icon.png)

You may start communicating with the bot by clicking on the on the bot icon.

![chat](chat-window.png)

### Running Haystack Service

1. Start the elasticsearch document store and initialize question-answer service (requires docker)

    ```bash
    python3 ./haystack/init_doc_store.py
    uvicorn app:app --reload --app-dir rest_api/
    ```

    This will create a new docker container called `elasticsearch` where all of the documents that can be queried will be stored. If this docker container ever stops you can either restart it from within docker dashboard or delete and recreate the container.

    This script also launches the REST API used for querying the Haystack service.

2. To access the Haystack API documentation, go to `http://127.0.0.1:8000/docs` in your browser. You should see the below image:

    ![Haystack api swagger documentation](haystack-api.png)

### Running API Tests

- To test that the API is functioning properly run the following:

    ```bash
    pytest api_tests/tests.py
    ```

---

[Back to Top](https://github.com/bhakthil/student-assist#ask-cci-bot)

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Docker, Elasticsearch,,##
Databases and services: Docker, Elasticsearch, Haystack,,##
Databases and services: Docker, Elasticsearch, Haystack,,##
Databases and services: Docker, Elasticsearch, Haystack,,##
Databases and services: Docker, Elasticsearch, Haystack,,##
Docker, Elasticsearch,,##
Databases and services: Docker, Elasticsearch, Haystack,,##
Databases and services: elasticsearch, Haystack,,##
Databases and services: Docker, Elasticsearch, Haystack,,##
Databases and services: elasticsearch, Haystack,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Docker, Elasticsearch, Haystack

## Purpose of external services

- **Docker**: Docker is used to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all parts it needs, such as libraries and other dependencies, and ship it all out as one package.
- **Elasticsearch**: Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.
- **Haystack**: Haystack is a framework for building search systems. It provides tools to index and query documents, and it integrates with Elasticsearch to provide advanced search capabilities.