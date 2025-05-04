REQUEST
Problem: This is a README file from a Rasa chatbot repository # RestaurantBot 🤖💬

**Your Personal Food Ordering Assistant**

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source-150x25.png?v=103)](https://github.com/s-4-m-a-n) 
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br/>

The Restaurant Bot is a proof of concept project powered by Rasa that aims to provide a seamless food ordering experience. With advanced natural language processing capabilities, it allows users to effortlessly place food orders, track their status, and receive personalized recommendations based on their preferences.

## Features

- Intuitive conversational interface for placing orders :white_check_mark:
- Real-time order tracking and updates :white_check_mark:
- Personalized recommendations based on user preferences :black_square_button:
- Multi-platform support (web, mobile, messaging apps) :black_square_button:
- Integration with popular food delivery services :black_square_button:

## Technology used
- Python (3.7.16)
- Docker (24.0.2, build cb74dfc)
- Docker compose (v2.17.3)
- Bootstrap 5.0

## Requirements
- Flask==2.2.5
- flask_sqlalchemy==3.0.3
- SQLAlchemy==1.4.48
- Requests==2.30.0
- reportlab==4.0.4
- rasa:3.5.6
- rasa-sdk:3.5.1

## Chatbot UI widget
- [Chatbot widget](https://github.com/Ani512/respobot-frontend)
  
## How to run

**1. Clone the repository:**

```bash
git@github.com:s-4-m-a-n/RestaurantBot.git
```

**2. Docker compose**

*:heavy_exclamation_mark: Make sure you have docker and docker compose installed on your system*
```bash
$ sudo docker compose up --build
```

**4. Train the model manually**

   - **get inside rasa-server container**
     
 ```bash
 $ docker exec -it rasa-server sh
 ```
    
   - **train rasa model**
     
 ```bash
 $ rasa train --fixed-model-name mymodel
 ```
## Endpoints
once the docker compose is up you can visit the following link to check out the chatbot

- `http://localhost:5000/chat`
  
- `http://localhost:5000/`

## Usage
- Interact with the ResBot through the chatbot web interface.
- Follow the prompts to place food orders, track their status, and explore personalized recommendations.

## Screenshots
![screenshot of chatbot UI](https://github.com/s-4-m-a-n/RestaurantBot/blob/main/screenshots/chatbot-ui.png)
![screenshot of order mgmt](https://github.com/s-4-m-a-n/RestaurantBot/blob/main/screenshots/order-mgmt.png)

## Demo
![Demo](https://github.com/s-4-m-a-n/RestaurantBot/blob/main/screenshots/demo.gif)

## Contributing
Contributions are welcome! If you'd like to contribute to the ResBot project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## Acknowledgements

We would like to express our gratitude to the open-source community for providing the necessary tools and resources to develop this project.


## LICENSE:
  It is an open source project and is being licensed under MIT LICENSE - [click me](https://github.com/s-4-m-a-n/RestaurantBot//blob/master/LICENSE) to get to the license file for more details.

## Contact
**For any inquiries or feedback, please reach out to us at `dhakalsumn739@gmail.com`.**
[![gmail](https://img.shields.io/static/v1.svg?label=contact&message=@me&color=9cf&logo=gmail&style=flat&logoColor=white&colorA=critical)](https://mail.google.com/mail/?view=cm&fs=1&to=dhakalsumn739@gmail.com) 
[![linkedin](https://img.shields.io/static/v1.svg?label=follow&message=@&color=grey&logo=linkedin&style=flat&logoColor=white&colorA=informational)](https://www.linkedin.com/in/suman-dhakal-2822a1198/)


        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Flask, flask_sqlalchemy, SQLAlchemy, Requests, rasa, rasa-sdk,,##
Flask-SQLAlchemy, SQLAlchemy, Requests,,##
Flask-SQLAlchemy, SQLAlchemy, Requests,,##
Flask, flask_sqlalchemy, SQLAlchemy, Requests, reportlab, rasa, rasa-sdk,,##
Flask-SQLAlchemy, SQLAlchemy, Requests,,##
Flask-SQLAlchemy, SQLAlchemy, Requests,,##
Flask-SQLAlchemy, SQLAlchemy, Requests,,##
Flask, flask_sqlalchemy, SQLAlchemy, Requests, rasa, rasa-sdk,,##
Flask, flask_sqlalchemy, SQLAlchemy, Requests, rasa, rasa-sdk,,##
Flask-SQLAlchemy, SQLAlchemy, Requests,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Flask-SQLAlchemy, SQLAlchemy, Requests, rasa, rasa-sdk

## Purpose of external services
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, making it easier to use SQLAlchemy with Flask applications.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for database interactions.
- **Requests**: A simple HTTP library for Python, used for making HTTP requests.
- **rasa**: An open-source machine learning framework for building AI assistants and chatbots.
- **rasa-sdk**: A toolkit for developing custom actions for Rasa, allowing the chatbot to perform specific tasks based on user input.