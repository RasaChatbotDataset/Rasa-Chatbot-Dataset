REQUEST
Problem: This is a README file from a Rasa chatbot repository # Using ChatGPT in a custom action to answer questions about data


Most Rasa chatbots fetch data from an API. E.g. in the financial-demo, a user can see their latest transactions.
Here, we have a dummy API returning restaurant results.

Using the ChatGPT API, we then allow users to ask questions *about* the data they've just been shown. 
We have an existing feature called [Knowledge Base Actions](https://rasa.com/blog/integrating-rasa-with-knowledge-bases/) which does the same thing. In comparison, using ChatGPT is much simpler, but also occasionally makes up wrong answers!


<img width="1173" alt="image" src="https://user-images.githubusercontent.com/5114084/222745358-84140a22-12c6-493e-b66e-0c94a20afec0.png">


Here's the data which the API has access to:

|    | Restaurants            |   Rating | Has WiFi   | cuisine   |
|---:|:-----------------------|---------:|:-----------|:----------|
|  0 | Mama's Pizza           |      4.5 | False      | italian   |
|  1 | Tacos el Cabron        |      4.6 | True       | mexican   |
|  2 | China Palace           |      3.2 | False      | chinese   |
|  3 | The Cheesecake Factory |      4.2 | True       | american  |
|  4 | Pizza Hut              |      3.8 | True       | italian   |
|  5 | Biryani Bowl           |      4.9 | False      | indian    |
|  6 | Burger King            |      2.6 | True       | american  |
|  7 | Taco Bell              |      3.5 | True       | mexican   |
|  8 | Freshii                |      4.7 | True       | healthy   |
|  9 | Panda Express          |      3.9 | False      | chinese   |
| 10 | McDonald's             |      2.3 | True       | american  |
| 11 | Sushi Roku             |      4.8 | True       | japanese  |
| 12 | Olive Garden           |      4   | True       | italian   |
| 13 | Chipotle               |      4.4 | True       | mexican   |
| 14 | Little Caesars         |      3.1 | False      | italian   |

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services:,- Dummy API,- ChatGPT API
API, ChatGPT API,,###
API, ChatGPT API,,###
Databases and services: ,- Dummy API,- ChatGPT API
Databases and services:,- Dummy API,- ChatGPT API
Databases and services:,- Dummy API,- ChatGPT API
API, ChatGPT API,,###
API, ChatGPT API
Databases and services: ,- Dummy API,- ChatGPT API
API, ChatGPT API,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Dummy API, ChatGPT API

### Purpose of external services
- Dummy API: This service provides a mock dataset of restaurant information, including details such as restaurant names, ratings, availability of WiFi, and cuisine types.
- ChatGPT API: This service is used to process and generate responses to user queries about the data provided by the Dummy API, leveraging the capabilities of the ChatGPT language model.