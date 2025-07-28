REQUEST
Problem: This is a README file from a Rasa chatbot repository # Knowledge Base Bot

This example bot uses a knowledge base to answer user's requests.

## What’s inside this example?

This example contains some training data and the main files needed to build an
assistant on your local machine. The `knowledgebasebot` consists of the following files:

- **data/nlu.yml** contains training examples for the NLU model
- **data/stories.yml** contains training stories for the Core model
- **actions/actions.py** contains the custom action for querying the knowledge base
- **config.yml** contains the model configuration
- **domain.yml** contains the domain of the assistant
- **endpoints.yml** contains the webhook configuration for the custom action
- **knowledge_base_data.json** contains the data for the knowledge base

## How to use this example?

To train your knowledge base bot, execute
```
rasa train
```
This will store a zipped model file in `models/`.

Start the action server by
```
rasa run actions
```

To chat with the bot on the command line, run
```
rasa shell
```

For more information about the individual commands, please check out our
[documentation](http://rasa.com/docs/rasa/command-line-interface).

## Encountered any issues?
Let us know about it by posting on [Rasa Community Forum](https://forum.rasa.com)!

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    - knowledge_base_data.json,,##
- knowledge_base_data.json,,##
- knowledge_base_data.json,,##
knowledge_base_data.json,,##
- knowledge_base_data.json,,##
- knowledge_base_data.json,,##
- knowledge_base_data.json,,##
- knowledge_base_data.json,,##
knowledge_base_data.json,,##
- knowledge_base_data.json,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
knowledge_base_data.json

## Purpose of external services
- **knowledge_base_data.json**: This file contains the data for the knowledge base that the chatbot uses to answer user requests.