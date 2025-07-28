REQUEST
Problem: This is a README file from a Rasa chatbot repository # Jokebot - Rasa Demo Bot

This is a Rasa demo bot. You can try the bot out at [https://avkana.com/jokebot](https://avkana.com/jokebot).

You can ask for Geek jokes, Corny jokes. Also, Kanye, Ron Swanson, Creed, Breaking Bad, Inspiring or Trump quotes.

## ToDo

- Brainy quote, `https://github.com/Hemil96/Brainyquote-API`
- Github Actions pipeline
- Google Assistant integration
- NLU test data
- Core test data
- rasa validate
- Support [multi-intents](https://blog.rasa.com/how-to-handle-multiple-intents-per-input-using-rasa-nlu-tensorflow-pipeline/?_ga=2.50044902.1771157212.1575170721-2034915719.1563294018)

## New Features

**Oct 2022**

- Upgrade to 3.0

**Jan 2021:**

- GitHub actions
  - Build actions docker image
- Creed quotes
- Kanye quotes, `https://api.kanye.rest/?format=text`

## Test Curl

```
curl --location --request POST 'http://localhost:5055/webhook' \
--data-raw '{      
  "next_action": "action_kanye",
  "sender_id": "postman",
  "tracker": {
    "sender_id": "default",
    "slots": {},
    "latest_message": {},
    "latest_event_time": 1535092548.4191391,
    "followup_action": "action_listen",
    "events": []
  },
  "domain": {
    "config": {},
    "intents": [],
    "entities": [],
    "slots": {}
  }
}'
```

```
curl --location --request POST 'http://rasa-production:5005/webhooks/rest/webhook' --header 'Content-Type: application/x-www-form-urlencoded' --data-raw '{"sender": "postman","message": "hello" }'
curl --location --request POST 'http://localhost/webhooks/rest/webhook' --header 'Content-Type: application/x-www-form-urlencoded' --data-raw '{"sender": "postman","message": "hello" }'
curl --location --request POST 'http://localhost:5005/webhooks/rest/webhook' --header 'Content-Type: application/x-www-form-urlencoded' --data-raw '{"sender": "postman","message": "hello" }'
```
        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    External services:,- Brainyquote-API,- Kanye Rest API
External services: Brainyquote-API, Kanye Rest API
External services:,- Brainyquote-API,- Kanye Rest API
External services: Brainyquote-API, Kanye Rest API
External services:,- Brainyquote-API,- Kanye Rest API
External services: Brainyquote-API, Kanye API
External services:,- Brainyquote-API,- Kanye Rest API
External services:,- Brainyquote-API,- Kanye Rest API
External services:,- Brainyquote-API,- Kanye Rest API
External services: Brainyquote-API, Kanye API
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Brainyquote-API, Kanye Rest API

Purpose of external services:
- Brainyquote-API: This service is used to fetch quotes from the Brainyquote database, providing users with a variety of inspirational and famous quotes.
- Kanye Rest API: This service is used to retrieve quotes from Kanye West, offering users unique and entertaining quotes from the artist.