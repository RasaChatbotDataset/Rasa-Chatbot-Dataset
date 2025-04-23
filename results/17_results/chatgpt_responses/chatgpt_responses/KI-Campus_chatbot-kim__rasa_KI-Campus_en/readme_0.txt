REQUEST
Problem: This is a README file from a Rasa chatbot repository # KI-Campus Chatbot "KIM"

## Training of the Model 

Choose the folder with the chatbot in English (KI-Campus_en) or in German (KI-Campus_de)

```sh
    rasa train
```

## Configuration

### Course Recommender Endpoint

> __NOTE__ Currently only supported for German chabot (`rasa/KI-Campus_de/`)

Create (or modify) the configuration file `kic_recommender.yml` in directory
```
    rasa/KI-Campus_de/
```

and add/modify configuration entry for Course Recommender Endpoint with the
base URL for the endpoint and the access token:
```yml
# This file contains the custom service endpoints your bot can use.

# recommender service (DFKI) configuration
recommender_api:
  url: "<base URL for recommender service endpoint>"
  token: "<recommender access token>"

```

## Usage

### Start the Rasa Server

```sh
    rasa run --enable-api
```

### Start the Action Server

```sh
    rasa run actions
```

NOTE the actions **must not** be started from within the `actions/` sub-directory, 
     but the `rasa` project's root directory (e.g. `rasa/KI-Campus_de/`),
     otherwise not all actions may be automatically started.

### Start for Development

Change configuration to _'for local development'_ endpoint in `endpoints.yml` in sub-directories
```
    rasa/KI-Campus_de/
    rasa/KI-Campus_en/
```

then (within the respective directory) start the chatbot shell with

```sh
    rasa shell
```

for testing logged-in user, get your `access-token` from the ki-campus website and start shell with

```sh
    rasa shell --conversation-id <access-token>
```


## Docker

In the outer project structure run:

### Docker Compose (de)

```sh
    docker-compose -f docker-compose_de.yml -p kicampus_de up --build
```

### Docker Compose (en)

```sh
    docker-compose -f docker-compose_en.yml -p kicampus_en up --build
```

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    recommender_api,,###
External services:,- Course Recommender Endpoint
- Course Recommender Endpoint,,###
- Course Recommender Endpoint,,###
- Course Recommender Endpoint,,###
Course Recommender Endpoint,,###
- Course Recommender Endpoint,,###
- Course Recommender Endpoint,,###
External services:,- Course Recommender Endpoint
- Course Recommender Endpoint,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Course Recommender Endpoint

## Purpose of external services

Course Recommender Endpoint: This service is used to provide course recommendations to users based on their preferences and interactions with the chatbot.