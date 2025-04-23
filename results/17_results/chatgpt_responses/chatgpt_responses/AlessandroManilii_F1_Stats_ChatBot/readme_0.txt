REQUEST
Problem: This is a README file from a Rasa chatbot repository # F1_Stats_ChatBot
Chatbot implemented through RASA framework on F1 statistics and generic info about races, pilots, circuits from 1950 season up to now.

Data retrival is made through 2 API:
 - Fast-F1: 
   - *pip install fastf1*
   - more info and code at:
      - https://github.com/theOehrly/Fast-F1 
      - https://theoehrly.github.io/Fast-F1/examples/index.html
 - Ergast:
   - more info at: http://ergast.com/mrd/
 
External library used:
- Request cache: *pip install requests-cache*
- Flask: *pip install flask*
  - run server through *python app.py*
- Spacy Model:
  - *pip install -U pip setuptools wheel*
  - *pip install -U spacy*
  - python -m spacy download en_core_web_md

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Fast-F1, Ergast
Fast-F1, Ergast, Request cache, Flask, Spacy Model,,##
Fast-F1, Ergast
Fast-F1, Ergast
Fast-F1, Ergast
Fast-F1, Ergast
Fast-F1, Ergast
Fast-F1, Ergast
Fast-F1, Ergast, Request cache, Flask, Spacy Model,,##
Fast-F1, Ergast, Request cache, Flask, Spacy Model,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Fast-F1, Ergast

Purpose of external services:
- Fast-F1: Used for retrieving detailed Formula 1 data and statistics.
- Ergast: Provides historical data on Formula 1 races, drivers, and circuits.