REQUEST
Problem: This is a README file from a Rasa chatbot repository # Formbot

The `formbot` example is designed to help you understand how the `FormAction` works and how
to implement it in practice. Using the code and data files in this directory, you
can build a simple restaurant search assistant capable of recommending
restaurants based on user preferences.

## What’s inside this example?

This example contains some training data and the main files needed to build an
assistant on your local machine. The `formbot` consists of the following files:

- **data/nlu.yml** contains training examples for the NLU model
- **data/stories.yml** contains training stories for the Core model
- **actions/actions.py** contains the implementation of a custom `FormAction`
- **config.yml** contains the model configuration
- **domain.yml** contains the domain of the assistant
- **endpoints.yml** contains the webhook configuration for the custom actions

## How to use this example?

Using this example you can build an actual assistant which demonstrates the
functionality of the `FormAction`. You can test the example using the following
steps:

1. Train a Rasa model containing the Rasa NLU and Rasa Core models by running:
    ```
    rasa train
    ```
    The model will be stored in the `/models` directory as a zipped file.

2. Run an instance of [duckling](https://rasa.com/docs/rasa/nlu/components/#ducklingentityextractor)
   on port 8000 by either running the docker command
   ```
   docker run -p 8000:8000 rasa/duckling
   ```
   or [installing duckling](https://github.com/facebook/duckling#requirements) directly on your machine and starting the server.

3. Test the assistant by running:
    ```
    rasa run actions&
    rasa shell -m models --endpoints endpoints.yml
    ```
    This will load the assistant in your command line for you to chat.

For more information about the individual commands, please check out our
[documentation](http://rasa.com/docs/rasa/command-line-interface).

## Encountered any issues?
Let us know about it by posting on [Rasa Community Forum](https://forum.rasa.com)!

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    duckling,,##
- Duckling,,##
duckling,,##
- Duckling,,##
duckling,,##
- Duckling,,##
duckling,,##
- Duckling,,##
Duckling,,##
duckling,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
duckling

## Purpose of external services
- **Duckling**: Duckling is used for extracting entities such as dates, times, and numbers from the user's input. It helps in understanding and processing user preferences more accurately.