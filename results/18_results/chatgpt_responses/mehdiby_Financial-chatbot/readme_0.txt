REQUEST
Problem: This is a README file from a Rasa chatbot repository # Financial-chatbot
In today's world, artificial intelligence (AI) is revolutionizing every domain it touches, including natural language processing (NLP) and finance. This project aims to leverage the power of AI to provide users with an agent capable of fluently conversing with them and providing them with real-time financial data whenever needed.

## Training the Model

To train the chatbot model, run the following command:

`rasa train`


This will train the model using the configuration specified in the `config.yml` file and the training data specified in the `data` directory.

## Running the Chatbot with Custom Actions

The Financial Chatbot has custom actions that enable it to scrape the web and provide users with real-time financial data such as currency exchange rates and stock prices.

To use these custom actions, start the action server by running the following command:

`rasa run actions`


This will start the action server on port 5055.

To start the chatbot server, run the following command:

`rasa run`


This will start the chatbot server on port 5005.

## Interacting with the Chatbot

### Using the Rasa Shell

To interact with the chatbot using the Rasa shell, run the following command:

`rasa shell`


This will open up a command-line interface where you can chat with the bot. Try asking it for financial data, such as:



### Using the Web Interface

To interact with the chatbot using the web interface, deploy the chatbot using the following command:

`rasa run --model models --enable-api --cors "*" `


This will start the chatbot server on port 5005 and enable the API.

Next, open the `index.html` file in your web browser. This will load the web interface for the chatbot. Type your message in the text box and press the "Send" button to chat with the bot. Try asking it for financial data, such as:

<div>
  <img src="images/1.PNG" alt="Image 1" width="250">
  <img src="images/2.PNG" alt="Image 2" width="250">
  <img src="images/3.PNG" alt="Image 3" width="250">
</div>


        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Web scraping,,##
Databases and services: Web scraping, Real-time financial data,,##
Databases and services: Web scraping,,##
External services: Web scraping,,##
External services: Web scraping,,##
External services: Web scraping,,##
External services: Web scraping,,##
Databases and services: Web scraping,,##
External services: Web scraping,,##
External services: Web scraping,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Web scraping

## Purpose of external services
Web scraping: Used to gather real-time financial data such as currency exchange rates and stock prices from various websites.