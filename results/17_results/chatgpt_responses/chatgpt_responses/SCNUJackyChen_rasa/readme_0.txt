REQUEST
Problem: This is a README file from a Rasa chatbot repository # Coffee Fun! -- Intelligent Coffee Ordering Chatbot

An end-to-end conversational system configured on the Flask framework, with a backend chatbot configured on the RASA framework running on Docker. The chatbot supports 3 use cases: Chitchat, Coffee order and Feedback. See our demo by clicking the picture below.

[![Demo](https://github.com/SCNUJackyChen/rasa/blob/master/pics/overview.png)](https://drive.google.com/file/d/1d4lvbny-Xwi0GmAkEFfn_gQfmta_6WPI/view?usp=sharing)


# How to use

## Docker Images
### RASA backend
We deploy the RASA backend in Docker, you can either build from Dockerfile or pull from our released image.

Use `docker build -t <image_name> .` to build a docker image locally.

Use `docker pull scnujackychen/coffeefun` to pull image remotely.

### MySql
The MySql Docker can be pulled from our released image.

Use `docker pull scnujackychen/rasa_mysql`

Unzip the data volumn `mysql.zip` to `/rasa/`.

## Create container

### MySql
`docker run -it -v path_to_mysql_data_volumn --name database scnujackychen/rasa_mysql:latest`

### RASA backend
`docker run -it --name rasa -p 5005:5005 --link database:db scnujackychen/rasa_coffeefun:latest`

## Run Flask
`python UI\app.py`

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    MySql,,#
MySql,,#
MySql,,#
MySql,,#
MySql,,##
MySql
MySql,,##
MySql
MySql,,#
MySql,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
MySql

# Purpose of external services
MySql: MySql is used as the database to store and manage data for the chatbot, such as user information, coffee orders, and feedback.