REQUEST
Problem: This is a README file from a Rasa chatbot repository # Samadhan – A Local Government Service QueryBot
 Samadhan aims to act as a virtual facilitator, using technology to provide the public with accurate and accessible information about government processes. Activities include a communication network that can provide guidance on steps required, documentation required and estimated timelines for tasks. The scope of the solution extends to a central location for feedback, providing and owning linked relationships as more knowledge has emerged in government agencies and citizens. It is built to accommodate scalability and ensure adaptability to evolving government policies. 🌐🔍💻📄📅📢🔄🏛️🤝📊🌱    

## Authors

- [Aarogya Bhandari](https://www.github.com/amewzzz)
- [Aayush Pokharel](https://github.com/aayushpkrl)
- [Piyush Luitel](https://www.github.com/PiyushLuitel-07)
- [Prashant Bhusal](https://www.github.com/prashant72-git)

## Demo video
[Click here for demo in youtube](https://www.youtube.com/watch?v=6Sh4Np_nWME)

## This is how our chatbot looks like
![Hello Samadhan](https://github.com/PiyushLuitel-07/Samadhan-A-Local-Government-Service-QueryBot/blob/main/Chatbot-Widget-main/58dbdc32-8422-4af7-86cb-2bc46d12bab9.gif)

## Features

- Information accessibility
- Guidance and assistance
- User-Friendly Interface
- Transparency and Accountability


## Installation

Install this project (open git bash terminal and type this code)

```bash
 git clone https://github.com/PiyushLuitel-07/Samadhan-A-Local-Government-Service-QueryBot
```

## Using the application
- Activate your environment.

- Install the required dependencies from requirements.txt
```bash
pip install -r requirements.txt
```

- train the model
```bash
rasa train
```

- After model is trained, run the following code in two different terminals simultaneously
```bash
rasa run actions
```
```bash
rasa run -m models --enable-api --cors "*" --debug
```

- Open the file Chatbot-Widget-main/index.html to see the actual working of our project.



    

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Rasa,,##
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