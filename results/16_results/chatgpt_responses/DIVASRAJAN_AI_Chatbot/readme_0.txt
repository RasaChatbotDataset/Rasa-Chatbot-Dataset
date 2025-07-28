REQUEST
Problem: This is a README file from a Rasa chatbot repository # AI_Chatbot
AI chatbot created using rasa

python 3.9

rasa init command gives the files which we want to create a chatbot in the specified folder.
what we want to do is just change it based on our need.

I created this as a basic restaurant booking chatbot.

create a database in mysql add details of restaurants 
created two 'action' functions to fetch the location and the restaurants in the specific location based on user's interst
used 'slot' to remember what was the location which user said to verify at the final point 

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services:,mysql
MySQL
MySQL
MySQL
MySQL
MySQL
MySQL
MySQL
Databases and services:,- MySQL
Databases and services: MySQL
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
MySQL

Purpose of external services:
MySQL: Used to create a database and store details of restaurants, which the chatbot can query to fetch information based on the user's location and interests.