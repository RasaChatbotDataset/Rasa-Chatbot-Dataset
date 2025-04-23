REQUEST
Problem: This is a README file from a Rasa chatbot repository # salama4ai-chatbot
chatbot based on rasa framework as an assessment NLP task for Master-linux company jan-2022
+ **Note**:- now the chatbot have an issue just because the endpoint that was provided by master-linux firm is not valid anymore, please replace the existing endpoint with a working one, and the model will work properly

## Objective:-
The goal is to create Rasa Chatbot that can provide answers for users questions about the Population and the capitel city of collecton of countries, where the chatbot use the restful API to get that information from third-party website

## initialization tips:-
to clone the repository:
```bash
git clone https://github.com/salama4ai/salama4ai-chatbot.git
```
to install rasa
visit https://www.youtube.com/playlist?list=PL75e0qA87dlEWUA5ToqLLR026wIkk2evk```
install anaconda or miniconda

to ensure that you installed anaconda successfully
```
conda -V
```
then open anaconda prompt, and update conda 
```bash
conda update conda
```
to create new virtual environment
```bash
conda create -n yourenvname python=3.8 
```
you must install python3.8 or 3.7 as rasa compatable with these two


create new folder and go to it and activate you environment
```bash
conda activate test_env
```
install rasa
```
pip install rasa
```
initialize you first project
```
rasa init 
```
if you need to train your bot after modifing files
```
rasa train
```
if you need to interact with your bot
```
rasa shell
```
or 
```
rasa interactive
```
if you use ```rasa interactive``` so you can train the bot by chatting and interacting with it 
if you write custom action so you need to open anaconda prompt and activate the bot and in the prompt run
```rasa run actions``` 
and leave it open in the background to be able to use the custom action with another prompt
you also can run shell in debug mode using ```rasa shell --debug```
and you can use ```rasa train --force``` to enforce retraining
if you make changes in action.py file you don't need to retrain again just rerun ```rasa run actions```

#
this work done by Ahmed Salama at JAN-2022

salama4ai@gmail.com

[github.com/salama4ai](https://www.github.com/salama4ai/)

[linkedin.com/in/salama4ai](https://www.linkedin.com/in/salama4ai/)




        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    External service: Restful API,,##
restful API,,##
restful API,,##
restful API, third-party website,,##
External services: restful API,,##
restful API,,##
Restful API,,##
External services: restful API,,##
restful API,,##
External service: Restful API,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Restful API

## Purpose of external services
Restful API: Used to fetch information about the population and capital city of various countries from a third-party website.