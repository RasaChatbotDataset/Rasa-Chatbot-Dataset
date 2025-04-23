REQUEST
Problem: This is a README file from a Rasa chatbot repository 

- in the intents.csv, i wasnt sure what wouldve been used to store the journal entries, quizzes, questions, requests , mood entries etc. , in the backend, so i put place holders. These should be replaced with actual calls to fetch jounral entries.

eg: view_mood_entries,List my mood entries,"['Here are your mood entries: {mood_entries}']"

app.py
- Includes routes for user registration, login, journal entries, mood entries, goals, conversations, requests, and quizzes.

chatbot.py
- Manages the chatbot interface and interactions with the Rasa server.
- Sends user inputs to the Rasa webhook and processes the responses.

create_tables.sql
- creates tables

populate_database.py (basically just for testing)
- Inserts records into the users, goals, journal entries, mood tracking, requests, quizzes, questions, and answers tables.


        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: SQL database, Rasa server
Databases and services: ,- Local database
Databases and services: ,- Local database
Databases and services: ,- Local database
Databases and services: SQL database, Rasa server
Databases and services: ,- Local database,- Rasa server
Databases and services: ,- Local database
Databases and services: SQL database, Rasa server
Databases and services: ,- Local database,- Rasa server
Databases and services: ,- Local database
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
SQL database, Rasa server

Purpose of external services:
- SQL database: Used to store user data, journal entries, mood entries, goals, conversations, requests, and quizzes.
- Rasa server: Manages the chatbot interface and processes user inputs to generate appropriate responses.