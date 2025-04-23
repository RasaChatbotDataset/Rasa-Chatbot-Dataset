REQUEST
Problem: This is a README file from a Rasa chatbot repository # Recipe Finding Chatbot
## Acknowledgment
This chatbot is based off of the pizza ordering chatbot found at https://github.com/Dingdong-LIU/Lab1_Chatbot_Rasa/tree/main/chatbot/02-forms-pizza-ordering-chatbot

## Install Anaconda
Install Anaconda via https://conda.io/projects/conda/en/latest/user-guide/install/index.html#

### Create a virtualenv via Conda
```bash
conda create -n rasa_env python=3.9
```
This will create a Conda virtual environment with <code>Python3.9</code>. Then you need to install <code>rasa</code> via <code>pip3</code>.

### Activate virtual environment
```bash
conda activate rasa_env
```
### Install rasa 3
```bash
pip3 install rasa
```

### Install edamam
```bash
python -m pip install py-edamam
```

### Uninstall uvloop
```bash
python -m pip uninstall uvloop
```
Note: this library leads to exceptions with forms
### Install Node.js & npm
1. If you are using `Apple Silicon Mac`, you can follow the guide here: https://devzilla.io/using-nodejs-14-with-mac-silicon-m1
2. If you are using `Intel Mac` or Unix-like OS, things are much simpler. 
   1. Install `nvm` - please follow the official guide [here](https://github.com/nvm-sh/nvm#install--update-script). 
   2. And use `nvm` to install `node.js` following [examples on GitHub](https://github.com/nvm-sh/nvm#install--update-script). We recommend installing version 14 via `nvm install 14`.
3. If you are using a windows computer, you can download it from here: https://nodejs.org/en/blog/release/v14.17.3

### Install yarn

```
npm install --global yarn
```

### Running the chatbot
First, clone the repository.
Then, open three terminal windows and activate rasa_env in all of them

In one window, run the action server:
```bash
rasa run actions
```

In another window, run the chatbot server:
```bash
rasa run --enable-api -p 5005 --debug --cors "*"
```

In the last window, launch the UI
```bash
python -m http.server 8889
```

The Chatbot can now be accessed at:  http://localhost:8889

## Links


*   [Rasa Forms Documentation](https://rasa.com/docs/rasa/forms)
*   [Rasa Project on GitHub](https://github.com/RasaHQ/conversationl-ai-course-3.x/tree/main/video-09-1-basic-forms)

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    edamam,,##
Edamam,,##
edamam,,##
Edamam,,##
edamam,,##
edamam,,##
edamam,,##
Edamam,,##
edamam,,##
edamam,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
edamam

## Purpose of external services
**Edamam**: This service is used to find recipes based on user input. It provides access to a large database of recipes and nutritional information.