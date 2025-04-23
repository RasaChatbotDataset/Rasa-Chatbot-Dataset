REQUEST
Problem: This is a README file from a Rasa chatbot repository # Interview-schedule-bot

The bot is used to converse with potential candidates. The chatbot gives a brief description of the company and the job role then asks the candidate if they are willing to take up the job and schedules an interview.

Developed using Rasa 3.x

## Steps to run the Bot

### Create and run a python environemnt 

Using Anaconda Prompt, run the following commands in the your preferred directory 
```bash
conda create -n envname python=3.6 anaconda
conda activate envname
```
Or refer [here](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/)

### Create a new rasa project

Run the following commmand after activating the python environment 
```bash
rasa init
```

### Install dependencies for the bot

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Run 'pip install rasa-sdk' in the python environment

### Overview of the files( also reffered to as dependencies)

`data/nlu/nlu.yml` - contains NLU training data

`data/nlu/rules.yml` - contains rules training data

`data/stories/stories*.yml` - contains stories training data

`actions.py` - contains custom action/api code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble

`tests/` - end-to-end tests

### Replace the files

Replace the default contents of the files with files in the repository 

### Run the bot

Use `rasa train` to train a model.

Then, to run, first set up your action server in one terminal window :
```bash
rasa run actions
```
In another prompt window, run the duckling server (for entity extraction):

```bash
docker run -p 8000:8000 rasa/duckling
```
Then to talk to the bot, run:
```
rasa shell --debug
```
Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working
under the hood. To simply talk to the bot, you can remove this flag.

Use should now be able to communicate with the bot in developer mode


        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    None
None
None
None
Docker Desktop, rasa/duckling,,###
None
None
Docker Desktop, rasa/duckling,,###
None
Docker Desktop, Duckling,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Docker Desktop, Duckling

### Purpose of external services

**Docker Desktop**: Used to run containerized applications, in this case, to run the Duckling server for entity extraction.

**Duckling**: A service used for extracting entities such as dates, times, and numbers from text, which is essential for scheduling interviews.