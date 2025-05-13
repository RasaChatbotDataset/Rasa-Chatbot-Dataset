# Service extraction: ChatGPT parameters

This folder contains the experimentation lead to study the best configuration of temperature and top_p parameters in a ChatGPT-4o model to identify external services used in a chatbot's backend. The experimentation considered all 24 combinations of the following values of temperature and top_p:

- **temperature**: 0, 0.25, 0.5, 1, 1.5, 2
- **top_p**: 0.01, 0.15, 0.5, 1


The service extraction process is composed of two phases, corresponding to the prompts shown below:
- **Extraction**: 10 repetitions of the same request to identify external services in a file.
- **Merge**: 1 request to merge and verify all the previous answers.

In the experimentation, for each configuration of parameters, we performed the extraction phase and then repeated the merge phase 5 times. 

## Chatbots
We studied the procedure over the following 11 chatbots:

| **id** | **Chatbot** | **# services** | **services** |
|----|  -------- | ------- | ----------| 
| 1 | [ABInBev Bot](https://github.com/Aryamaan23/IVR-chatbot/tree/main/ABInBev%20Bot)       |  6  | Twilio, Google Calendar, Authorize.net, Geopy, OpenCage Geocode, SMTP|
| 2 | [Assistant Bot](https://github.com/SergioMadrid22/assistant_bot_rasa) | 5 | Google Calendar, OpenWeatherMap, Google Generative AI , Pollinations, El Pais RSS Feed
| 3 | [Chatbot2](https://github.com/EryanDe/chatbot2) | 0 | |
| 4 | [Doctor Friende](https://github.com/pengyou200902/Doctor-Friende) | 1 | Neo4j |
| 5 | [Financial Bot](https://github.com/RasaHQ/financial-demo) | 1 | SQLalchemy|
| 6 | [Helpdesk Assistant](https://github.com/RasaHQ/helpdesk-assistant)| 1 | ServiceNow |
| 7 | [MainP0K Bot](https://github.com/MainP0k/Bot_Rasa) | 4 | SQLite, www.regal.fr, www.economie.gouv.fr, www.osmozbistro.com |
| 8 | [Mindcare](https://github.com/Roopesh519/Mindcare-Conversation-Chatbot-Rasa-Framework) | 0 | |
| 9 | [Rasa Customer Service](https://github.com/ashus3868/RasaCustomerService) | 0 | |
| 10 | [Rasa KB Bot](https://github.com/RasaHQ/kb-demo-chatgpt) | 2 | OpenAI, Local CSV |
| 11 | [THD Bot](https://github.com/THD-AI-2023/AIN-B-3-Assistant-Systems) | 1 | Local JSON |

## Evaluation metrics
To evaluate the results and compare different parameter configurations we computed precision, recall and f-score of each configuration based on the following definitions:

- **True Positive (TP)**: a service used in the file and identified by the procedure.
- **False Positive (FP)** a service not used in the file but identified by the procedure.
- **False Negative (FN)**: a service used in the file but not identified by the procedure.

**Precision**
$$
\text{Precision} = \frac{TP}{TP + FP}
$$

**Recall**
$$
\text{Recall} = \frac{TP}{TP + FN}
$$

#### F-score

$$
F-score = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

> Since with chatbots with zero services the procedure of 10 requests always identified zero services with each configuration, these chatbots were excluded from the merge phase and the final parameter comparison.

## Folder Structure

There is a folder for each chatbot with the following content:
- **actions.py**: the action backend file used in the experimentation.
- **10_extraction_requests.csv**: the responses of the 10 extraction requests.
- **5_merge_requests.xlsx**: the responses of the 5 merge requests and evaluation metrics, computed for each repetition and as average.

The overall comparison between the average precision, recall and f-score of each parameter configuration is presented in file **evaluation_metrics.xlsx**

> Note that {temperature: 1.5, top_p: 1} and {temperature: 2, top_p: 1} were excluded from the merge process and final evaluation since the responses received are random sequences of characters. 