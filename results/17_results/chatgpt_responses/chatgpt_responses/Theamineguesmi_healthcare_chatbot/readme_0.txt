REQUEST
Problem: This is a README file from a Rasa chatbot repository <p align="center"><img src="./assets/bot.png" width="10%"></p>
<h1 align="center">Customer Care Bot</h1>
<p align="center">Customer care bot for ecomm company which can solve faq and chitchat with users, can contact directly to team.</p>

<p align="center">
  <img src="https://img.shields.io/github/pipenv/locked/python-version/horizon733/customer-care-chatbot">
  <img src="https://img.shields.io/github/pipenv/locked/dependency-version/horizon733/customer-care-chatbot/rasa?color=blueviolet&label=Rasa">
</p>

<p align="center">
  <img src="https://img.shields.io/github/repo-size/horizon733/customer-care-chatbot">
</p>

## 🛠 Features
- [x] Basic E-commerce FAQ
- [x] Basic chitchats
- [x] Out of Scope
- [x] Contact us form
- [x] Send Emails

## ⚡ Quick Setup
- Initialize a virtual environment via:
- Conda:
```bash
conda create --name rasaenv python=3.7
```
- virtualenv
```bash
virtualenv -p python3.7 rasaenv
```
- use pipenv
```
cd /customer-care-chatbot
pipenv install
```

## 🧪 Testing
- Train bot
```
rasa train
```
- Test bot on shell
```
rasa shell
```
- start `rasa` server
```bash
rasa run --enable-api --cors "*" --debug[Optional] -p {PORT}[optional]
```
- start `actions` server
```
rasa run actions -p {PORT}[Optional]
```

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