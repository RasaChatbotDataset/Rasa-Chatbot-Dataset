REQUEST
Problem: This is a README file from a Rasa chatbot repository # AICTE Chatbot

 <ul style="list-style-type:square;">
  <li>AI based Chatbot to generate answers to queries based on FAQs
using the RASA 3.1 and BERT model.</li>
  <li>BERT Model helps to classify the questions relevancy with an
accuracy of 70% .</li>
  <li>Relevance question dataset is automatically updated by the questions
asked by the user, and is being stored in MYSQL database.</li>
  <li>Voice chat-feature is also provided which enables users to continue their conversation verbally to avoid thier physicall efforts.</li>
</ul> 

## Installation

Python and Rasa needs to be installed

```bash
sudo apt-get install python3.6
```

```bash
python -m pip install --upgrade pip rasa
```

## Usage

Go to the actions folder and run

```bash
rasa run actions.py
```
```bash
rasa run --enable-api --cors="*"
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Screenshots of portal

![alt text](https://i.ibb.co/vLWwVWh/Screenshot-447.png)

![alt text](https://i.ibb.co/jMTGBb0/Screenshot-448.png)

![alt text](https://i.ibb.co/N2wTMVq/Screenshot-449.png)

![alt text](https://i.ibb.co/n0rG2Mt/Screenshot-451.png)

![alt text](https://i.ibb.co/zrRh1Jg/Screenshot-450.png)

![alt text](https://i.ibb.co/Hp5HPWW/Screenshot-452.png)

![alt text](https://i.ibb.co/gTm8pX1/Screenshot-453.png)

![alt text](https://i.ibb.co/gmhPbjg/Screenshot-454.png)

![alt text](https://i.ibb.co/DpkD8qZ/Screenshot-455.png)




        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    MYSQL,,##
MYSQL,,##
MYSQL,,##
MYSQL,,##
MYSQL,,##
MYSQL,,##
MYSQL,,##
MYSQL,,##
MYSQL,,##
MYSQL,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
MYSQL

## Purpose of external services

MYSQL: Used to store and update the relevance question dataset based on the questions asked by the user.