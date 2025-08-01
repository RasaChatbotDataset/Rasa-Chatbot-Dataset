REQUEST
Problem: This is a README file from a Rasa chatbot repository [![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]

# Stock Recommender with OpenAI Chatbot Integration

Welcome to the GitHub repository for the Stock Recommender system, enhanced with an OpenAI Chatbot interface. This innovative tool is designed to assist users in making informed stock investment decisions by leveraging the power of AI and advanced analytics. 

## Features

- Stock Recommendations: Utilizes advanced algorithms to analyze market trends and provide personalized stock recommendations.
- OpenAI Chatbot Integration: Engage with our AI-powered chatbot for interactive queries about stock insights and investment advice.
- Unit Tests: Ensures reliability and performance through comprehensive unit testing, including tests for the OpenAI chatbot functionalities.

## Demo Videos

Get a closer look at our Stock Recommender system in action through these demo videos:

- [Chatbot Demo](https://youtu.be/M_kXf1QOYpA) 
- [Recommender Demo](https://youtu.be/iXdAlRiB-s0) 

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- streamlit
- rasa
- yfinance
  
Additionally you'll need:
- openai api key


1. Clone the repository:
```bash

git clone https://github.com/ostweg/Stock-Recommender.git
cd Stock-Recommender
```
2. Navigate to Rasa Chatbot, open two terminals & execute it
```bash
cd chatbot
rasa run actions # in first terminal
rasa shell # in second terminal
```
3. Navigate to OpenAI Chabot & execute it
```bash
cd chatbot
streamlit run main.py
```
4. Navigate to Recommender
```bash
cd stockrecolib/recommender
streamlit run app.py
```


[contributors-shield]: https://img.shields.io/github/contributors/ostweg/Stock-Recommender.svg?style=for-the-badge
[contributors-url]: https://github.com/ostweg/Stock-Recommender/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/ostweg/Stock-Recommender.svg?style=for-the-badge
[issues-url]: https://github.com/ostweg/Stock-Recommender/issues

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    External services: OpenAI, yfinance,,###
openai, yfinance,,##
External services: OpenAI, yfinance,,###
- yfinance,- openai,,###
- yfinance,- openai,,###
- yfinance,- openai,,###
External services: OpenAI, yfinance,,###
- yfinance, openai,,##
openai, yfinance,,##
- yfinance,- openai,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
OpenAI, yfinance

## Purpose of external services

- OpenAI: Used for the AI-powered chatbot interface to provide interactive queries about stock insights and investment advice.
- yfinance: Utilized to fetch stock market data and trends for analysis and recommendations.