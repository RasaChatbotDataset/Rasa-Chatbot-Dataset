REQUEST
Problem: This is a README file from a Rasa chatbot repository ### SHOPYVERSE - RASA AI-based chatbot - GPT bot 

This Program include Backend, Rasa chatbot and Gpt bot for both Telegram user group and Meatverse integration.
For the first step and runnig locally documentation

## Steps for local run

you can define openai api key in .env file

cd  .../{project-folder}

python3 -m venv venv

source venv/bin/activate   =>for linux and wsl2

./venv/bin/activate.ps     =>for windows

pip install -r requirements.txt    =>for first run

python3 -m spacy download en_core_web_md   =>for first run

cd .../backend-shopyverse 

python app.py

cd .../rasa_chatbot 

rasa run actions

rasa run --enable-api



        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: OpenAI API, Telegram, Meatverse,,###
Databases and services: openai, spacy,,###
Databases and services: openai, spacy,,###
Databases and services: OpenAI, Telegram, Meatverse,,###
OpenAI API,,###
Databases and services: OpenAI, Telegram, Meatverse,,###
Databases and services: OpenAI API, Spacy
Databases and services: openai, spacy
Databases and services: openai, spacy,,###
OpenAI API,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
OpenAI API, Telegram, Meatverse, Spacy

## Purpose of external services
- **OpenAI API**: Used for generating responses and leveraging GPT capabilities.
- **Telegram**: Used for integrating the chatbot with Telegram user groups.
- **Meatverse**: Used for integrating the chatbot with the Meatverse platform.
- **Spacy**: Used for natural language processing tasks such as tokenization and named entity recognition.