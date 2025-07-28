REQUEST
Problem: This is a README file from a Rasa chatbot repository # Chatbot SART
As part of the end-of-year project (PFA) as engineering students at ENSIAS, we chose to work on the implementation of a chatbot for a stock management application for a clothing store . Our project was to develop a chatbot, named "Chatbot SART - Style Assistant and Retail Technology", which was integrated into the application. This chatbot uses artificial intelligence, speech recognition, speech synthesis and natural language processing techniques to intuitively interact with users.
The main objective of this chatbot is to assist users with their stock management needs, by providing information on available products, stock levels, orders, etc.

<img src="chatbot-sart.png">

## Built with
* RASA
* Flask
* Bootstrap

## To run the bot

* Create a new virtual environment by choosing a Python interpreter and making a .\\venv directory to hold it:

    `C:\> python3 -m venv ./venv`
* Activate the virtual environment:

    `C:\> .\venv\Scripts\activate`

* First make sure your pip version is up to date:

    `pip3 install -U pip`

* To install Requirements:

    `pip3 install -r requirements.txt`

* Finally run the bot using bash terminal:

    `$ ./run_bot.sh`

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: RASA, Flask, Bootstrap,,##
Databases and services: RASA, Flask, Bootstrap,,##
SQLite, Google Cloud Speech-to-Text, Google Cloud Text-to-Speech,,##
Databases and services: RASA, Flask, Bootstrap,,##
SQLite, Google Cloud Speech-to-Text, Google Cloud Text-to-Speech,,##
SQLite, Google Cloud Speech-to-Text, Google Cloud Text-to-Speech,,##
Databases and services: None,,##
SQLite, Google Cloud Speech-to-Text, Google Cloud Text-to-Speech,,##
None
Databases and services: RASA, Flask, Bootstrap,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
SQLite, Google Cloud Speech-to-Text, Google Cloud Text-to-Speech

## Purpose of external services
* **SQLite**: A lightweight, disk-based database that doesn't require a separate server process and allows access to the database using a nonstandard variant of the SQL query language.
* **Google Cloud Speech-to-Text**: A service that converts audio to text by applying powerful neural network models in an easy-to-use API.
* **Google Cloud Text-to-Speech**: A service that converts text into natural-sounding speech using deep learning models.