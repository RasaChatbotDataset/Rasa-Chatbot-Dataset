REQUEST
Problem: This is a README file from a Rasa chatbot repository # rasabot_transhist
# RASA- Chatbot

This is simple chatbot to interact and findout the balance and the transaction history.

## REQUIRED!!
    - python 3.8.0(minimum version)

## Installing

1. Create the [Python Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and activate it:

    - python3 -m venv venv

    - venv/Scripts/activate

2. Install rasa framework:
    - pip install rasa

3. Train the model
    - rasa train
    
4. Run the actions to host it and open another terminal to load the trained model that lets you talk to your assistant on the command line.
    - rasa run actions          - rasa shell

5. Bot is ready to intereact
   
## Sample Conversation with chatbot.
![Screenshot (65)](https://github.com/rambabu44/rasabot_transhist/assets/48267686/40492fb4-42d5-4313-997d-e94daeb0ba07)



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