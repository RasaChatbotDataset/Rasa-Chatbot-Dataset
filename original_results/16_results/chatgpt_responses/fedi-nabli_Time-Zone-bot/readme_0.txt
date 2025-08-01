REQUEST
Problem: This is a README file from a Rasa chatbot repository # Time Zone Bot

The time zone bot is bot created using the rasa framework, it shows an example of how to create a simple or even more complex chatbots with the rasa framework without
any need to have a deep understanding a chatbot.

This project is perfect for:
- People who are experienced in ML and ChatBot creations and want to learn new technologies
- As well as beginners in the field of chat bots and want to have a general understanding of how it works

# Installation:
**Recommended way**\
You need to have installed:
- [Pyhon 3.9 or above](https://www.python.org/downloads/release/python-390/)
- [Rasa](https://rasa.com/docs/rasa/installation/installing-rasa-open-source/)

If you want to or already have went through the hassle of installing Python and Rasa, you can ```git clone``` this repository, then ```cd Time-Zone-Bot```.

# Running the project:
- To train the model run ```rasa train```, if it doesn't work try running ```python -m rasa train```, otherwise check your installation.
- To run the model run ```rasa shell```, if it doesn't work try running ```python -m rasa shell``` to talk with the bot.
- to run the NLU model run ```rasa shell nlu```, if it doens't work try running ```python -m rasa shell nlu``` to see the accuracy and entities
- **Important**\
- run the custom actions before running the shell by ```rasa run actions```, if it doens't work ```python -m rasa run actions```.

# Screenshots
<img src="./demo/bot_response.png" />
<img src="./demo/bot_response_2.png" />

- to stop the running bot type: ```/stop```

<img src="./demo/stop_bot.png" />

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