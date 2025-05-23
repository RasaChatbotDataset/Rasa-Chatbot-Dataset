REQUEST
Problem: This is a README file from a Rasa chatbot repository # astri-the-chatbot
Astri is a chatbot specifically for satellite applications. Astri is powered by Rasa and will continue to improve over time.

## Installation
Astri uses the index folder to hold the necessary data structures it uses to search and provide information back to the user. The specific files it needs are:
- acronyms.json {Key value pair - acronym :: Acronym Meeting}
- parts.json {Key value part - part/subsystem :: Description}
- ...fault files...

Spacy requires a small package to be downloaded using the command. Right now this is only used for the dev-tools

    python3 -m spacy download en_core_web_sm

## OpenAI Instructions

The user must have an openAI account to use the openAI features. Specifically, the API key needs to be generated from the website and stored in the actionConfig.yml file

## Running the server

    rasa train
    rasa run -m models --enable-api --cors "*"
    rasa run actions

# Docker Setup

## Extend the Rasa SDK Image

    docker build . -t rasa/rasa-sdk:3.4.0

## Create the docker network

    docker network create elastic

## Start the network

    docker run --name es-node01 --net elastic -p 9200:9200 -p 9300:9300 -t docker.elastic.co/elasticsearch/elasticsearch:8.5.3
    docker run --name kib-01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.5.3

Pause - startup of Elastic for the first time creates user id and passwords that are needed to log in. Those need to be updated in the actions/actionConfig.yml before continuing.

    docker run -v $(pwd):/app --name astri-nlu -p 5005:5005 --net elastic rasa/rasa:3.4.0-full run -m models --enable-api --cors "*"
    docker run --name astri-act -p 5055:5055 -v $(pwd)/actions:/app/actions -v $(pwd)/index:/app/index --net elastic rasa/rasa-sdk:3.4.0

## For Apple Silicon Macs

### Beta steps only...

Since Rasa does not offer arm64 docker images, new ones need to be built from the arm64 Python base image. Two custom Dockerfiles are included to build these images.

    docker build -f Dockerfile_nlu_arm64 -t astri_nlu:1.0 .
    docker build -f Dockerfile_act_arm64 -t astri_act:1.0 .

The docker run commands after then break out as follows:

    docker run -v $(pwd):/app --name astri-nlu -p 5005:5005 --net elastic astri_nlu:1.0 run -m models --enable-api --cors "*"
    docker run --name astri-act -p 5055:5055 -v $(pwd)/actions:/app/actions -v $(pwd)/index:/app/index --net elastic astri_act:1.0

## Setup Elastic

When starting the first time, Elasticsearch has a set of startup instruction that need to be followed. See this site for instructions for startup: [https://www.elastic.co/guide/en/elasticsearch/reference/8.5/docker.html](https://www.elastic.co/guide/en/elasticsearch/reference/8.5/docker.html)

## Populate the search index

In dev-tools, there is a script that parses through a list of URLs for text to create the index. You can also use your own index or scrapper to populate the Elasticsearch data

# Dev tools use

## textProcessing.py

This tool can take a webpage, pdf or text file and generate some program unique data for Astri use.

    python textprocessing.py (inputData)

Note that this tool uses nltk data and the following items need to be installed

    python -m nltk.downloader stopwords
    python -m nltk.downloader punkt
    python -m nltk.downloader averaged_perceptron_tagger

If you are having SSL issues connecting to nltk (replace X with your versio of Python)

    bash /Applications/Python 3.X/Install Certificates.command
        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    OpenAI, Elasticsearch,,##
OpenAI, Elasticsearch,,##
OpenAI, Elasticsearch,,##
- OpenAI,- Elasticsearch,,##
- OpenAI,- Elasticsearch,,##
OpenAI, Elasticsearch,,##
OpenAI, Elasticsearch,,##
OpenAI, Elasticsearch,,##
OpenAI, Elasticsearch,,##
Elasticsearch, OpenAI,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
OpenAI, Elasticsearch

## Purpose of external services
- OpenAI: Used for leveraging OpenAI's API to enhance the chatbot's capabilities with advanced natural language processing and understanding.
- Elasticsearch: Used for indexing and searching data to provide quick and relevant information to the user.