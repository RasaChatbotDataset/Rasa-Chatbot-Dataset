REQUEST
Problem: This is a README file from a Rasa chatbot repository # Sample chatbot with rasa stack

It uses the rasa stack (rasa core/nlu/actions) to implement a simple bot which responds user messages.

## Run on local machine

#### Using docker
Both action server and rasa-core runs as separate processes in the same container. Rename the .env-sample to .env and optionally update the API_KEYs, TOKENs etc.
```
docker build -t rasa-chatbot .
docker run -it --rm -p 5005:5005 --env-file $(pwd)/.env rasa-chatbot
```
It starts a webserver with rest api and listens for messages at localhost:5005

#### Test over REST api

```bash
curl --request POST \
  --url http://localhost:5005/webhooks/rest/webhook \
  --header 'content-type: application/json' \
  --data '{
    "message": "Hi"
  }'
```
**Response**
```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 59
Access-Control-Allow-Origin: *

[{
  "recipient_id": "default",
  "text": "Hi, how is it going?"
}]
```

## Try the bot using in terminal
```bash
docker run --rm --volume $(pwd):/app --env-file $(pwd)/.env -it\
          --workdir /app rasa-chatbot bash ./scripts/start_shell.sh
```

## Run using docker compose
Optionally to run the actions server in separate container start the services using docker-compose. The action server runs on http://action_server:5055/webhook (docker's internal network). The rasa-core services uses the config/endpoints.local.yml to find this actions server

```
docker-compose up
```
#### Train Rasa model
The repository already contains a trained Rasa model at models directory. To retrain the model you can run:
```bash
docker run --rm --volume $(pwd):/app \
          --workdir /app rasa/rasa \
          train --fixed-model-name rasa-model \
          --config config.yml
```

## Deploy to Heroku
On heroku free tier we can start two containers using two dynos, but there isn't a way for the containers to communicate with each other on Heroku. So, we push everything (actions server/rasa core/nlu) in the same container.

```bash
heroku container:push -a rasa-chatbot web
heroku container:release -a rasa-chatbot web
```

Another option would be to create a separate app altogether for actions server (nlu server can also be run as a separate app), which then can communicate with each other over http.

## Integration with Facebook
rasa supports integration with multiple channels. Apart from exposing the REST api over http, we can integrate with facebook. 

Go to https://developers.facebook.com and creat an app. We can handle messages sent to a facebook page from our app. To do so add messenger to the facebook app and subscribe to a page. Update app secret and page token in config/credentials.yml. On the facebook app, update the webhook url to the deployed heroku app (https://rasa-chatbot.herokuapp.com/webhooks/facebook/webhook).



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
None
None
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
NO