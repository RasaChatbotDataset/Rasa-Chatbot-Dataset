REQUEST
Problem: This is a README file from a Rasa chatbot repository Docker Hub [image](https://hub.docker.com/r/stephens/jokebot/tags?page=1&ordering=last_updated)

Notes on building the action agent image:

- Setup build using [rasa-action-server-gha](https://github.com/RasaHQ/rasa-action-server-gha)

# Local Action Agent Build

```sh
cd actions
export CR_PAT=xxx
./build.sh
#docker build -t stephens/jokebot:test .
#docker tag stephens/jokebot:test stephens/jokebot:1.0.2
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