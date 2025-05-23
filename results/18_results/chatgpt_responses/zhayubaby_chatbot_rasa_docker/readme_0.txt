REQUEST
Problem: This is a README file from a Rasa chatbot repository # chatbot_rasa_docker
This is a rasa chatbot including docker files and configurations, you can use this chatbot in docker containers.  
  
Because this program has been deployed on the server, it cannot be run in a local IDE (such as vscode, pycharm). You need to deploy it to docker and start it before it can run on the local web page.  
  
If you have deployed and started it on docker, you can open the web page and enter 'localhost:8088'. You will enter the rasa chatbot conversation web page. You can enter some designed conversations and check the effect.  
  
The design of the dialogue has been placed in story.txt, which you can use as a reference.  
  
The deployment method and configuration of docker will be introduced below.  
  
# docker configurations
First, check out the RASA document for docker running  
  
![docker](https://github.com/zhayubaby/chatbot_rasa_docker/assets/121445047/17c6f8b0-5686-4f6b-bece-90c4931029f5)  

  If you want to simplify the process, you can follow my steps below:  

    1. First download the entire project locally and open it in the IDE (take vscode as an example).  

    2. Open the terminal in vscode and enter the command 'docker-compose up -d' to deploy the docker container.  

<img width="505" alt="docker_2" src="https://github.com/zhayubaby/chatbot_rasa_docker/assets/121445047/4d0b0954-e864-427d-a810-f3780f6c4391">


    3. The docker-compose.yml file is already in the project. After the deployment is completed, open docker desktop and the following effect will be displayed, which means success.  

<img width="1075" alt="docker_3" src="https://github.com/zhayubaby/chatbot_rasa_docker/assets/121445047/78f64591-ce9f-4dd8-b322-e23177a228d4">


    4. Next, enable the chatbot action to run the container.  

    5. open the web page and enter 'localhost:8088' to start the rasa chatbot conversation page.  

  # Rasa chatbot cloud server
  The project has been deployed to the cloud, but it has an expiration date and cannot be used for a long time. If it exceeds the expiration date, please use docker to deploy it.  

  You can open the web page and enter the url: 'http://39.107.124.206:8088/' to open the same web page, because the project has been deployed to the cloud.  

  However, the URL has an expiration date from October 9, 2023 to January 1, 2024. The URL will not be available after the expiration date.


  


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