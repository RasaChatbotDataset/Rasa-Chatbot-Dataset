REQUEST
Problem: This is a README file from a Rasa chatbot repository # rhit_IRPA_2023

Rose-hulman Institute of Technology Class of Senior Design 2023 IRPA Chatbots Project

## Setup instructions:

1. Install Anaconda.

2. Open Anaconda Terminal.

3. Run "conda env create -f environment.yml" in anaconda terminal this will create an environment called irpa_chatbot and install the necessary libraries.

4. Activate the environment that was created by running "conda activate irpa_chatbot"

5. Run "pip install farm-haystack==1.16.0"

6. Create an .env file with the following fields:
  - SECRET_KEY
  - ROOT_USERNAME
  - ENVIRONMENT #Options: development, production

  See the .env_template file for an example.
  SECRET_KEY specifies a a key used to create authorization token for the admin
  ROOT_USERNAME specifies the initial root administrator user who can access the system and add admins. It should be a Rose-Hulman username.
  ENVIRONMENT specifies the environment the software is in. The options are development and production.

## Running Locally

- Open four anaconda terminal and each should be in the irpa_chatbot environment. (conda activate irpa_chatbot). Each
  terminal is for starting each of the services below:

  ### Starting Rasa API
  In the anaconda terminal, run "python -m  rasa run --cors "*" --enable-api"
  
  ### Starting Rasa Action Server
  In the anaconda terminal, run "python -m rasa run actions"

  ### Starting Backend API
  In the anaconda terminal, run "uvicorn general_api:app --reload"

  ### Starting Frontend
  1. cd into chatbot_app folder
  2. Run "npm install"

## Testing:
Open anaconda terminal, cd into the project directory
### Test Rasa Model:
 Type rasa test in the terminal. The test results will be in failed_stories.yml in the results directory.
### Unit Test and Integration Test
 Don't need to cd into test directory. At the project's root directory run the following command:
   - To run all test: python -m unittest discover tests test*.py
   - To run individual test: python -m unittest tests/{name of test}.py 
      - For example: python -m unittest tests/test_knowledgebase.py
      - Note: all test files should start with prefix "test"


        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: farm-haystack, uvicorn, npm,,##
farm-haystack,,##
Databases and services: farm-haystack, uvicorn,,##
Databases and services: farm-haystack, uvicorn,,##
Databases and services: farm-haystack, uvicorn,,##
Databases and services: farm-haystack, uvicorn,,##
Databases and services: farm-haystack, uvicorn, npm,,##
Databases and services: farm-haystack, uvicorn,,##
Databases and services: farm-haystack, uvicorn, npm,,##
Databases and services: farm-haystack, uvicorn,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
farm-haystack, uvicorn, npm

## Purpose of external services
- farm-haystack: Used for implementing search and retrieval functionalities within the chatbot.
- uvicorn: A lightning-fast ASGI server implementation, used to run the backend API.
- npm: A package manager for JavaScript, used to manage and install dependencies for the frontend application.