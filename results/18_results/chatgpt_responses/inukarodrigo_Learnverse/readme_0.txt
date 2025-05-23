REQUEST
Problem: This is a README file from a Rasa chatbot repository # Learnverse

A Flask-based web application that aids students in improving weaknesses by generating practise exams. 

## Overview

This Flask-based web application helps advanced level ICT students by generating customized practice exams, offering a virtual classroom to communicate with teachers, predicting potential exam grades, and providing an AI chatbot for additional assistance.

## Features

- Firebase authorization
- Exam paper generation based on users' performance
- Allows user to request specific lessons and receive custom exam papers tailored to his/her needs
- Leaderboard after successful completion of test
- Also, user can see the solution after doing a question in a test
- User can chat with AI chabot to clarify the doubts
- Enables users to share resources with one another and engage in chat communication.

## Screenshots
#### Landing Page:
![Landing Page](screenshots/Landing_page.png)

#### Login Page:
![Login Page](screenshots/Login_page.jpeg)

#### Selection Page:
![Selection Page](screenshots/Selection_page.png)

#### Exam Paper Selection:
![Exam Paper Selection](screenshots/Exam_paper_selection.png)

#### Leaderboard:
![Leaderboard](screenshots/Test_Summary.png)

#### Virtual Classroom:
![Virtual Classroom](screenshots/Virtual_Classroom.jpeg)

#### General Chat Bot - Learny:
![image](https://user-images.githubusercontent.com/88397747/228536170-19ee831c-d81d-49a8-b27b-b8542e633422.png
)
# How To Use
### Prerequisites

Before you begin, ensure that you have met the following requirements:

- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/) version 2021.2 or higher

You can install PyCharm Community Edition by downloading and running the installer for your operating system from the official JetBrains website.

### 1. Clone this repository

```bash
git clone https://github.com/inukarodrigo/Learnverse.git
```

### 2. Install [Pipenv](https://pipenv.pypa.io/en/latest/)

### 3. Start the bot in a Conda environment
1 First create a conda environemt
open conda prompt in 

- open [Anaconda](https://www.anaconda.com/products/distribution) prompt
- change to the project file
> Projects\Learnverse\AI Chatbot Guide
- Create the Conda environment using the following command
```
conda create --name rasaenv python=3.7.6
```
- Activate the Conda environment using the following command
```
conda activate rasaenv
```
2 Install following packages
```
conda install ujson
conda install tensorflow
```
3 Install rasa using pip(currently no conda install version)
```
pip install rasa
```
Run the following command to run the bot in the web application
```
rasa run -m models --enable-api --cors "*"
```
Then the Bot will start
## Contributors

We would like to thank the following contributors for their help with this project:

- [Lisara Gajaweera](https://github.com/LI3ARA)
- [Maneth Subawickrama](https://github.com/Maneth22)
- [Haneek Ahamed](https://github.com/HaneekAhamed)


        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Firebase,,##
Firebase, Anaconda,,##
Firebase,,##
Firebase,,##
Firebase,,##
Firebase,,##
Firebase,,##
Firebase,,##
Firebase,,##
Firebase,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Firebase, Anaconda

## Purpose of external services

- **Firebase**: Used for user authentication and possibly for storing user data and exam results.
- **Anaconda**: Used to manage the Conda environment for running the Rasa chatbot.