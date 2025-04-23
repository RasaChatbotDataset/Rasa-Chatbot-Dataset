REQUEST
Problem: This is a README file from a Rasa chatbot repository # Concertbot

Example bot that contains only story data.

## What’s inside this example?

This example contains some training data and the main files needed to build an
assistant on your local machine. The `concertbot` consists of the following files:

- **data/stories.md** contains training stories for the Core model
- **actions/actions.py** contains some custom actions
- **config.yml** contains the model configuration
- **domain.yml** contains the domain of the assistant
- **endpoints.yml** contains the webhook configuration for the custom actions

## How to use this example?

To train a model, run
```
rasa train core -d domain.yml -s data/stories.md --out models -c config.yml
```

To create new training data using interactive learning, execute
```
rasa interactive core -d domain.yml -m models -c config.yml --stories data
```

To visualize your story data, run
```
rasa visualize
```

To run a Rasa server, execute
```
rasa run actions&
rasa run -m models --endpoints endpoints.yml
```

To chat with your bot on the command line, run
```
rasa run actions&
rasa shell -m models
```

For more information about the individual commands, please check out our
[documentation](http://rasa.com/docs/rasa/command-line-interface).

## Encountered any issues?
Let us know about it by posting on [Rasa Community Forum](https://forum.rasa.com)!

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