REQUEST
Problem: This is a README file from a Rasa chatbot repository # COVID-19 Chatbot with Rasa 2.0: open source conversational AI(currently migrating to Rasa 3.x)

## Table of Contents
1. [Introduction](#introduction)
2. [COVID-19 data](#COVID-19_data)
3. [Conversational flow](#Conversation_Flow)
4. [Demonstration](#demo)
6. [Installation](#Installation)
7. [References](#References)
## Introduction
<a name="introduction"></a>

As natural language processing (NLP) technology and chatbot systems over the past few years have evolved quickly, also the usefulness of chatbots has increased. The motivation of chatbots is productivity; they have an instant access to information they refer to and are efficient in assisting users. (Brandtzaeg, 2017, *Why people use chatbots*. COVID-19 chatbot is an excellent use case example for the technology.

The content of a chatbot consists of the personality, conversation flows and the information it can deliver to the user. Personality is created by interactions and responses and by acting differently in different situations. These responses should be designed so that it maximises the engagement between the bot and the user (Katz, 2019, *The Ultimate Guide to chatbot personality*, Chatbots Magazine). The COVID-19 chatbot described here aims to use these principles, however due to the efforts required, in a rather minimalistic way leaving plenty of room for future improvements. e.g. in the area of how to handle chitchat.

## COVID-19 data
<a name="COVID-19_data"></a>
The COVID-19 data format chosen here is defined by (https://api.rootnet.in/covid19-in/stats/history), which provides COVID-19 data freely for developers. 

## Conversation Flow
<a name="Conversation_Flow"></a>
The conversation is initiated by the end-user. The user starts with a greeting "hi" , "hey" etc. The bot responds with the list that user can ask to bot. if user chooses option 1. The bot asks for the state name. When user enters the state name , the bot replies with the details for cases.




## Demonstration:
<a name="demo"></a>
<br>
 ### Sample Demonstration Images:<br>
 Chatbot's Intro Interface:<br>
<img src="https://user-images.githubusercontent.com/59523836/209435980-fd31fa24-82d5-4235-8dbc-96c034a0625d.png"></img><br>
 Chatbot's Chat Interface:<br>
<img src="https://user-images.githubusercontent.com/59523836/209436003-8f377aaf-f502-444b-9706-eda27508cc9f.png"></img><br>
 Chatbot's Tracker Interface:<br>
<img src="https://user-images.githubusercontent.com/59523836/209436020-a88e9660-59cc-40b9-a607-4d84367de6e6.png"></img><br>
Deployed Chatbot's Telegram interface:<br>
<img src="https://user-images.githubusercontent.com/59523836/209436030-9b391ae9-08e3-464c-acac-890b5efe3bae.png"></img><br>

 <br><br>
 
 
 
 
 
 
 


## Installation
<a name="Installation"></a> 
Installation assumes existing installation of miniconda or anaconda. 
https://www.anaconda.com/

### pip3 & Rasa

Below are the simple steps for creating a virtual environment, install pip3 and Rasa Open Source 2.0.

```
conda create -n RasaEnv python=3.7.6 
conda activate RasaEnv
conda install -c anaconda pip3
pip3 install rasa==2.8.11  
```
In case of issue, please refer to Rasa Open Source installation pages: 
https://rasa.com/docs/rasa/installation/

### Creating and initialising a new project:

```p
mkdir rasa
cd rasa
rasa init --no-prompt
```
This will create a new directlry, under which rasa creates all necessary directories and files.

Replace all files in the rasa directory with the files in the project.

## Train the model and run the bot

Train the model with command 

```
rasa train
```

There are additional actions that need to be started before starting the bot evaluation. These are in ```actions.py``` file. To do so, run below commands on two different terminals: 

```
rasa run actions
```

Start the discussion with rasabot:

```
rasa shell
```

## Starting the model on deployable server

Terminal 1(starting ngrok on default port of rasa 5005):
```
ngrok http 5005
```
copy paste the url in the credentials file.

Terminal 2(start bot):
```
rasa run
```
Terminal 3(start actions file):

```
rasa run actions
```
Now just go to "Covid-bot-Aazim" on telegram and start using! 



## References
<a name="References"></a>
    - Rasa. (n.d.). Rasa: Open source conversational AI. URL: https://rasa.com
    
    

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Rootnet API,,##
Rootnet API,,##
Rootnet API,,##
Rootnet API,,##
Rootnet API,,##
Rootnet API,,##
Rootnet API,,##
Rootnet API,,##
- Rootnet API,- Ngrok,- Telegram,,##
Rootnet API,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Rootnet API, Ngrok, Telegram

## Purpose of external services
- Rootnet API: Provides COVID-19 data for developers.
- Ngrok: Allows secure introspectable tunnels to localhost, useful for testing and development.
- Telegram: Platform for deploying and interacting with the chatbot.