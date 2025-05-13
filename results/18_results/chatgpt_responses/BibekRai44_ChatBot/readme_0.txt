REQUEST
Problem: This is a README file from a Rasa chatbot repository 
# ChatBot

A chatbot built with Rasa. The chatbot is designed to handle conversations and provide responses based on predefined intents and actions.


## Deployment

To run this project 

```bash
  git clone https://github.com/BibekRai44/ChatBot
```
```
  pip install -r requirements.txt
```
```
  cd ChatBot
```
let actions running  in first terminal 
```
  rasa run actions
```
run below line in second terminal
```
  rasa train && rasa shell --debug
```
# Customization

You can customize the chatbot's behavior by modifying the following files:

1) data/nlu.yml: Define the training data for the chatbot's NLU (Natural Language Understanding) model.

2) data/stories.yml: Define the conversation flow and dialogue management of the chatbot.
3) actions/actions.py: Implement custom actions for the chatbot, such as calling external APIs or performing specific tasks.
4) domain.yml: Define the chatbot's domain, including intents, entities, actions, and responses.

Make sure to retrain the chatbot (rasa train) after making any changes to these files.

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