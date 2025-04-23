REQUEST
Problem: This is a README file from a Rasa chatbot repository ## ChainBuddy decentralized chatbot

### Overview

This repository contains a chatbot powered by the Rasa framework. This chatbot is designed to support with operations on the Flow blockchain.

### Getting Started

- Deploy test tokens in [ChainBuddy.Flow](https://github.com/lukaszidz/ChainBuddy/tree/master/ChainBuddy.Flow)
- Launch steps:
  - [ChainBuddy.Api](https://github.com/lukaszidz/ChainBuddy/tree/master/ChainBuddy.Api) - Python Flask API for Flow Blockchain communication
  - [ChainBuddy.Chat](https://github.com/lukaszidz/ChainBuddy/tree/master/ChainBuddy.Chat) - Rasa chat framework
  - [ChainBuddy.UI](https://github.com/lukaszidz/ChainBuddy/tree/master/ChainBuddy.UI) - User interface for chatbot communication

### License

ChainBuddy is an open-source software licensed under the [MIT](https://github.com/lukaszidz/ChainBuddy/blob/master/License.txt).

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
- Flow Blockchain,- Python Flask API,- Rasa,- ChainBuddy.UI,,###
None
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Flow Blockchain, Python Flask API, Rasa

### Purpose of external services

- **Flow Blockchain**: Used for deploying and managing test tokens.
- **Python Flask API**: Facilitates communication with the Flow Blockchain.
- **Rasa**: Provides the chatbot framework for building and managing the chatbot's conversational capabilities.