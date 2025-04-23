REQUEST
Problem: This is a README file from a Rasa chatbot repository # News-Article-Chatbot

Chatbot that can link the user to articles, given a topic (person, place, date, etc.). Articles were scraped from the Wall Street Journal and NPR, and processed using Spacy. The chatbot was made using Rasa.

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: Wall Street Journal, NPR, Spacy, Rasa
Wall Street Journal, NPR, Spacy, Rasa
Databases and services: Wall Street Journal, NPR, Spacy, Rasa
Wall Street Journal, NPR, Spacy, Rasa
Databases and services: Wall Street Journal, NPR, Spacy, Rasa
Wall Street Journal, NPR, Spacy, Rasa,,##
Wall Street Journal, NPR, Spacy, Rasa
Wall Street Journal, NPR, Spacy, Rasa
Wall Street Journal, NPR, Spacy, Rasa,,###
Databases and services: Wall Street Journal, NPR, Spacy, Rasa
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Wall Street Journal, NPR, Rasa

Purpose of external services:
- Wall Street Journal: Provides articles that the chatbot can link to based on user queries.
- NPR: Provides articles that the chatbot can link to based on user queries.
- Rasa: Framework used to build and manage the chatbot.