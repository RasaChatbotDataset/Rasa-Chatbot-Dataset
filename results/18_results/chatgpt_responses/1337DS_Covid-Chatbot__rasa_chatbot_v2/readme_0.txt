REQUEST
Problem: This is a README file from a Rasa chatbot repository # Covid-Chatbot
The chatbot should answer the questions of the user to topics concerning Covid-19.

The bot will display r-index and similar up-to-date statistics as well as information on how to prevent and cope with covid. A focus of the bot is on creating statistics as plots. To achieve this the text input is interpreted and reasonable x and y-axis labels are applied. The data for the plot is received through APIs from credible sources like the Robert Koch Institute.

## File structure
The current development state is in the ```rasa_chatbot_v2``` folder. The ```docker_rasa_chatbot``` was our attempt to dockerize the application. However, this was not successfull. The ```Chatbot-Widget``` folder contains the files for the frontend of the chatbot.

## Screencast

https://user-images.githubusercontent.com/77493377/150161105-5233421c-d4e4-45ea-b6e3-c74d02b8a443.mp4


## Possible questions for Carl 

- Whats the incidence in Germany?

- Whats the incidence in Mannheim?

- Whats the incidence in Cottbus?

- Give me the incidence map of Germany?

- What are Covid-19 symptoms?

- How many died last week?

- I think i have corona

> In case Carl doesnt recognize your request, he will give tips to rephrase your question.


## Installation Instructions:

1. *Rasa is required for the execution. If you don't have Rasa installed yet then you can do this e.g. in a Conda environment. For this you should use the command:*

```
pip3 install -U --user pip && pip3 install rasa
```

 *For more information, please follow the instruction of the official Rasa documentation: https://rasa.com/docs/rasa/installation*

2. *Start rasa*

```
rasa run -m models --enable-api --cors "*" --debug
```

3. *Start actionserver*

```
rasa run actions
```

4. *Start Imageserver*

```
python3 picture_server.py
```

5. *Open index.html*
Click on the [index.html](Chatbot-Widget/Chatbot-Widget-main/index.html) file to see the frontend with our mascot Carl Corona 🤖.

## Team members:

Andreas Edte  
Canberk Alkan  
Dominic Viola  
Jendrik Hülsmeyer  
Johannes Damke  
Killian Ebi  


## Some evaluations 

Evaluation metrics for the rasa_chatbot.


<table border="0" columns=2 align="center">
    <tr>
    <col>
        <td><img src="https://user-images.githubusercontent.com/77493377/150163110-d96783e9-4ffc-4537-acaa-847050161655.png" alt="" width=50%></img></th>
        <td><img src="https://user-images.githubusercontent.com/77493377/150163119-e4829812-0448-4d34-8474-b95094213a58.png" alt="" width=100%></img></th>
    </col>
    </tr>
    <tr>
    <col>
        <td><img src="https://user-images.githubusercontent.com/77493377/150163122-2203c17d-6f21-47e4-886b-44b192e2ba3b.png" alt="" width=50%></img></th>
        <td><img src="https://user-images.githubusercontent.com/77493377/150163142-b965cedb-ae13-4e7f-80c3-239bc81df46b.png" alt=""  width=100%></img></th>
    </col>
    </tr>
</table>



        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Robert Koch Institute
- Robert Koch Institute API,,##
- Robert Koch Institute API,,##
- Robert Koch Institute API,,##
Databases and services:,- Robert Koch Institute API
- Robert Koch Institute API,,##
Robert Koch Institute,,##
Robert Koch Institute
- Robert Koch Institute API,,##
Robert Koch Institute,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Robert Koch Institute API

## Purpose of external services

- **Robert Koch Institute API**: This service is used to fetch up-to-date statistics and data related to Covid-19, such as incidence rates, death counts, and other relevant information.