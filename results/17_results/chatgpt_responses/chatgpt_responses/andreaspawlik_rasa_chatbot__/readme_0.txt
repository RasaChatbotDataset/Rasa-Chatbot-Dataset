REQUEST
Problem: This is a README file from a Rasa chatbot repository # rasa_chatbot

## Introduction

This repo is a result of the Zeiss ZDP hackathon challenge in 06/2022. 

## Goal

Build a chatbot to implement a self-service channel to customers. 

- Provide Q&A in a customer self-service scenario
- Use RASA technology for building contextual text-based assistants
- Bot should respond to questions of device-specific information
- Bot should use data from tabular database

## Getting Started

### Requirement

- python 3.7 or 3.8
- pandas
- rasa 3.1 ([Here for step-by-step installation](https://rasa.com/docs/rasa/installation/))
- fuzzywuzzy: `pip install fuzzywuzzy`

### Starting the bot

Code has been only set up locally. To run the bot, follow these steps: 

1. Start the action server.
    1. Navigate to your rasa directory. 
    2. `rasa run actions` . This starts the server for the custom action. 
    3. Keep this tab open and running when testing the bot. 
2. Start the bot. 
    1. Open a second terminal 
    3. Train the bot by `rasa train`
    2. Start the bot by `rasa shell`
    2. You can now chat with the bot :) 

## Known issues

- slot values persist after inquiry. 
- still some typo intolerance. 
- asking "how much is an iphone 13", and the bot asks "which brand do you want?" (bot should infer the brand!)

## Future features

Due to time constraint, following nice-to-have features haven't been implemented yet:

- Run bot on a server
- Use endpoint to connect bot with MS teams
- if an item could not be found (e.g., Samsung iphone), the bot should propose an alternative (e.g., "did you mean Apple iphone?")
- Implementation of different languages (DE, CN etc)
- More semantic logics, e.g. “give top-tier smartphone” -> return the most phones
- Contextual understanding

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    pandas, fuzzywuzzy,,##
pandas, fuzzywuzzy,,##
pandas, fuzzywuzzy,,##
pandas, fuzzywuzzy,,##
- tabular database,,##
Databases and services:,- tabular database,- MS teams,,##
pandas, fuzzywuzzy,,##
Databases and services: tabular database,,##
pandas, fuzzywuzzy,,##
- tabular database,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
tabular database, MS teams

## Purpose of external services

- tabular database: Used to store and retrieve device-specific information for the chatbot to provide accurate responses.
- MS teams: Intended for future implementation to connect the bot with Microsoft Teams for broader accessibility and integration.