REQUEST
Problem: This is a README file from a Rasa chatbot repository # rasa-weather-bot

This bot answers questions about weather in a given city.

![Screenshot 2022-12-07 at 17 40 48](https://user-images.githubusercontent.com/23726630/206238847-17586f10-9b68-4e88-878a-68dbfb8703f0.png)

It uses OpenWeatherAPI to fetch the data. You can create a free account at https://openweathermap.org/, generate an API key and store it in creds.py (please note that you need to create this file from scratch).

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    OpenWeatherAPI
OpenWeatherAPI,,###
OpenWeatherAPI
OpenWeatherAPI
OpenWeatherAPI,,##
OpenWeatherAPI
OpenWeatherAPI
OpenWeatherAPI
OpenWeatherAPI
OpenWeatherAPI
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
OpenWeatherAPI

### Purpose of external services
OpenWeatherAPI: This service is used to fetch weather data for a given city.