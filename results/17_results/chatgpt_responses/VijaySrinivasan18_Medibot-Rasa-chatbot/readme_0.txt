REQUEST
Problem: This is a README file from a Rasa chatbot repository # MediBot-A-RASA-chat-Bot

Chat Bot using RASA Framework for health care industry.This Bot can assist the users to book appointment, confirm the appointment status and users can enquire about usage and side effects of any medicine. 
Bot will web scrape that information and will provide it to the user. Appointment details would be stored in SQL server using pyodbc.  

This bot has 3 major functionalities.
It can be used to book appointment, confirm the exising appointment and to know about the uses, side effects and dosage  of an medicine/tablet.
Custom actions has been created to do web scrapping from third party websites when information about any medicine has been asked for.
When users ask to book appointment, RASA forms would be triggered to get the information about First name, Last name, appointment date from user and these information would be added to sql server table , appointment number would be generated and provided to user.
When user ask to confirm their appointment status, another Rasa form would be used to get the appointment number which would have been provided while booking appointment , connects to sql server to check status of that appointment using given appointment number.


Tools:  Python and sql 
Libraries:Bs4,lxml,requests,pyodbc,pandas,regex,nltkpickle,google search,rasa_sdk,Flask.
        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    SQL server, third party websites, Google search,,###
SQL server, third party websites, Google search,,###
SQL server, third party websites, Google search,,###
SQL server, third party websites, Google search,,###
Databases and services: SQL server, third party websites, Google search
SQL server, third party websites, Google search,,###
SQL server, third party websites, Google search
SQL server, third party websites, Google search,,###
SQL server, third party websites, Google search,,###
SQL server, third party websites, Google search,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
SQL server, third party websites, Google search

## Purpose of external services

- **SQL server**: Used to store and retrieve appointment details.
- **Third party websites**: Used for web scraping to gather information about medicines, including their uses, side effects, and dosage.
- **Google search**: Utilized to find relevant third-party websites for web scraping.