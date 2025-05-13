REQUEST
Problem: This is a README file from a Rasa chatbot repository # KI-Campus Chatbot

## Training of the Model 

Choose the folder with the chatbot in English (KI-Campus_en) or in German (KI-Campus_de)

```sh
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