REQUEST
Problem: This is a README file from a Rasa chatbot repository # Get start
```bash
rasa run actions
rasa run
```

## Sent the first message
```bash
$headers = @{
    'Content-type' = 'application/json'
}

$body = @{
    text = 'Hello, World!'
} | ConvertTo-Json

Invoke-WebRequest -Uri 'https://hooks.slack.com/services/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' -Method Post -Headers $headers -Body $body
```
## Screenshot of the APP
![image](https://github.com/Incredible88/Chatbot-with-LLM-and-RASA/assets/60803217/dafbdd6b-83ce-45dc-b7c0-a19c022c48ba)

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    External services: Slack
External services: Slack,,##
External services: Slack,,##
External services: Slack,,##
External services: Slack,,##
External services: Slack,,##
Slack,,##
Slack,,##
Slack,,##
External services: Slack,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Slack

## Purpose of external services
Slack: Used for sending messages to a Slack channel via a webhook.