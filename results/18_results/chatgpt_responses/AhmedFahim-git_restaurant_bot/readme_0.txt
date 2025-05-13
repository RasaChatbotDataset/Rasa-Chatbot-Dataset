REQUEST
Problem: This is a README file from a Rasa chatbot repository # Restaurant Bot

Restaurant Bot is a simple chat bot that searches for restaurants, coffee houses, or both near given locations.

This is a sample project. It uses [Rasa](https://rasa.com/) as the chat bot framework and the [FOURSQUARE Places API](https://developer.foursquare.com/docs/places-api-overview) to search for the places of interest.

In order to use the chatbot first install Rasa in a virtual environment and activate it. Clone and move into the repository, and run the following command.

```terminal
rasa train
```

This may take a while as it trains the machine learning model.

Once the model is trained, in one terminal run the following command.

``` terminal
rasa run actions
```

Then in another terminal run the following command

``` terminal
rasa run --enable-api --cors='*'
```

Finally open the index.html file in the Chatbot-UI folder using your browser.

![The final chat bot!](/images/chatbot_UI.gif "The end result")

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    FOURSQUARE Places API,,##
FOURSQUARE Places API,,###
FOURSQUARE Places API,,##
FOURSQUARE Places API,,###
FOURSQUARE Places API,,###
FOURSQUARE Places API,,###
FOURSQUARE Places API,,###
FOURSQUARE Places API,,##
FOURSQUARE Places API,,##
FOURSQUARE Places API,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
FOURSQUARE Places API

## Purpose of external services
- **FOURSQUARE Places API**: This service is used to search for restaurants, coffee houses, or both near given locations.