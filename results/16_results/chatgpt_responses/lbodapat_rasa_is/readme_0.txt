REQUEST
Problem: This is a README file from a Rasa chatbot repository # Chatbots to Combat Disinformation 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Implemented using RASA framework:
[**Suraj Bodapati**](https://www.linkedin.com/in/suraj-bls/)

Deception Awareness & Resilience Training (DART) NSF Convergence Accelerator

## Abstract
- Build a conversational AI agent to combat disinformation at scale by targeting senior citizens with scams to get personal information.
- The idea is to direct the senior citizens to Deception Awareness and Resiliency Training(DART) post being scammed by the conversational agent.
- [**Documentation**](https://github.com/lbodapat/rasa_is/blob/master/report.pptx.pdf)

### Datasets:
[**End-to-End Trainable Non-Collaborative Dialog System**](https://arxiv.org/abs/1911.10742): https://gitlab.com/ucdavisnlp/antiscam

### Installation and Running the code
1. [**Install RASA**](https://rasa.com/docs/rasa/installation/installing-rasa-open-source/)
2. Clone the repository
3. RUN command on CLI - ```rasa train```
4. To test the model RUN command on CLI - ```rasa shell```
5. To test the model in DEBUG mode, RUN command on CLI - ```rasa interactive```
6. In the new terminal window RUN command on CLI - ```rasa run actions``` This is required to run the action server.
7. Finally In another new terminal run the Duckling Extractor in Docker. ```sudo docker run -p 8000:8000 rasa/duckling```

### Output Screenshot

![Alt text](/Notebooks/output.png?raw=true "Output ScreenShot")

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Duckling Extractor,,###
Duckling Extractor,,###
- Duckling Extractor,- Rasa,,###
Duckling Extractor,,###
Duckling Extractor,,###
- Duckling Extractor,- Rasa,,###
Duckling Extractor,,###
Duckling Extractor,,###
Duckling Extractor,,###
- Duckling Extractor,- RASA,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Duckling Extractor, Rasa

### Purpose of external services
- **Duckling Extractor**: Used for extracting structured information from text, such as dates, times, and numbers.
- **Rasa**: The framework used to build, train, and deploy the conversational AI agent.