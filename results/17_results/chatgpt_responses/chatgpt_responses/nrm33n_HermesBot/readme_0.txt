REQUEST
Problem: This is a README file from a Rasa chatbot repository # HermesBot :cowboy_hat_face:

<p align="center"> 
A <a href="https://rasa.com/">Rasa</a>-based chatbot that translates text from English to several other languages using the 
  <a href="https://pypi.org/project/translate/">translate</a> Python module. 
  Rasa uses a Dual Intent and Entity Transformer (DIET) for NLP/NLU and trains using min-min and min-max algorithms. HermesBot also uses memoization and rule-based policies. In addition to the translate module, I also included an emoji package so it's a little more fun to interact with :zany_face:
</p>

## Run the bot  
Since Rasa x is no longer free, you can speak to it on the command line by running 
`rasa run actions` and `rasa shell`on separate terminals. 

## Testing 
In tests, it can identify commands pretty well. Check out the confusion matrix with `rasa test`. The failed tests and other info is in the results folder.

## Visualization 
Take a look at the flow of conversation: 
 <p align="center">
<img src="https://user-images.githubusercontent.com/84393679/218781894-d4dcb9f8-a9f1-4cf1-a449-4d4141aaea3e.png" width=500 height=500>
</p>

You can see this a little clearer in graphs.html.

## Telegram
 Rasa makes it pretty easy to connect to other voice and chat platforms. Here it is as a telegram bot: 
<p align="center">
<img src="https://user-images.githubusercontent.com/84393679/218571208-0d7a5cfe-2909-40a2-9092-e6ccb3877917.png" width=300 height=700>
</p>

### Connect to Telegram
Run `ngrok http 5005` to obtain secure remote URL. Use this for webhook_url in credentials.yml file. 

Fill out the other sections by contacting @BotFather on telegram and setting up a new bot. 

Make sure to comment out the rasa localhost url in credentials.yml 


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
translate, ngrok, Telegram

## Purpose of external services
- translate: This service is used to translate text from English to several other languages.
- ngrok: This service is used to obtain a secure remote URL for connecting the chatbot to Telegram.
- Telegram: This service is used to deploy the chatbot as a Telegram bot, allowing users to interact with it through the Telegram platform.