REQUEST
Problem: This is a README file from a Rasa chatbot repository ![Eva greeting](https://github.com/fenjenahwe/NLI-EVA0/blob/V2/screenshot.png "Greeting EVA")

# Demo-Video

https://www.youtube.com/watch?v=U4JLH5BoXQQ


# NLI-EVA

Before you get started, you need to get some servers running:

### Rasa actions

Run this command in the folder:

`rasa run actions`

### Rasa chatbot

A pretrained model is provided. You can always retrain according to edits by running:

`rasa train`

Run this command to get the Rasa server running:

`rasa run -m models --enable-api -p 5055 --cors "*" --credentials credentials.yml`

### Python server (interface-rasa)

Install the libraries needed in the pyserver.py* file, install uvicorn and run this command (macos) to get the python server running:

`uvicorn pyserver:app --reload`

### Interface

(commands for macos)

`install sudo npm install -g http-server`

Run a local server: 

`http-server`

visit http://localhost:port/ to access the interface and finally interact with EVA!


### avatar

The 3D avatar used was downloaded and rigged from https://www.mixamo.com/#/?page=1&type=Character

Javi Agenjo's libraries (LiteGL and Rendeer) were used for the 3D canvas.  

### Weather API

To access the weather API, provide your API key in the ActionGetCurrWeather.py file.
        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Weather API,,###
Weather API,,###
Weather API,,###
External services: Weather API,,###
Weather API,,###
External services: Weather API,,###
Weather API,,###
Weather API,,###
- Weather API,,###
Weather API,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Weather API

### Purpose of external services

Weather API: This service is used to fetch current weather information.