REQUEST
Problem: This is a README file from a Rasa chatbot repository # AI-Chatbot

This project is designed to create an interactive chatbot using Rasa,
integrated with a MySQL database for user authentication.
The chatbot provides various functionalities, including:

- Greeting users
- Understanding their moods
- Responding to queries

Additionally, the project includes a visualization component
to illustrate the flow of conversation using D3.js and Dagre-D3 libraries.

## Features

### Chatbot Functionality:

- Handles various user intents, such as greetings, mood tracking, and service inquiries.
- Provides tailored responses based on user input, including positive and negative feedback paths.

### Database Integration:

- User authentication is facilitated through a MySQL database.
- Secure password handling using `getpass` to ensure user credentials are not exposed.

### Visualization:

- An HTML page visualizes the Rasa Core conversation flow.
- Uses D3.js and Dagre-D3 for interactive and dynamic graph rendering.

## Usage

- Interact with the chatbot through the command line or a connected frontend interface.
- Utilize the visual representation to understand the flow of conversations and actions taken by the bot.

## Contributors

Samu, Mika, Samuel, Zehra, Jukka

## Ohjelmistotuotantoprojekti

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    MySQL,,##
MySQL,,##
MySQL,,##
MySQL,,##
MySQL,,##
MySQL,,##
MySQL,,##
MySQL,,##
MySQL,,##
MySQL,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
MySQL

## Purpose of external services

### MySQL:
MySQL is used for user authentication, storing user credentials securely, and managing user data.