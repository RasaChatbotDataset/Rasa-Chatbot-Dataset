REQUEST
Problem: This is a README file from a Rasa chatbot repository # openWHO Chatbot v2

## Training of the Model 

```sh
    cd rasa/openWHO_{LANGUAGE}/
    rasa train
```

## Usage

### Start the Rasa Server

```sh
    rasa run --enable-api
```

### Start the Action Server

```sh
    cd actions/
    rasa run actions
```

## Docker

In the outer project structure run:

```sh
    docker-compose up --build
```


### Docker Compose (en)

```sh
    docker-compose -f docker-compose_en.yml -p openWHO_en up --build
```

### Docker Compose (es)

```sh
    docker-compose -f docker-compose_es.yml -p openWHO_es up --build
```

### Docker Compose (zh)

```sh
    docker-compose -f docker-compose_zh.yml -p openWHO_zh up --build
```
        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    None
None
None
None
None
None
None
None
None
None
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
NO