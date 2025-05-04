REQUEST
Problem: This is a README file from a Rasa chatbot repository # Rasa Chatbot for Product Negotiation

This project is a chatbot built using Rasa, an open-source machine learning framework for automated text and voice-based conversations. The primary function of this chatbot is to negotiate prices for products, specifically for items like the Samsung Galaxy S10 and iPhone 8.

## Features

- Responds to basic greetings and farewells.
- Engages in small talk about the user's mood.
- Conducts price negotiations for Samsung Galaxy S10 and iPhone 8.
- Custom action to handle price negotiation logic.

## Installation

To run this project, you need to have Python installed on your machine. The project was developed using Python 3.9.

### Clone the Repository

```bash
git clone https://github.com/Kheem-Dh/RasaNegotiationChatbot.git
cd RasaNegotiationChatbot
```

## Setup Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other projects or system-wide packages.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install Dependencies

Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Configuration

`endpoints.yml`
Make sure the endpoints.yml file is properly set up for the action server:

```bash
action_endpoint:
  url: "http://localhost:5055/webhook"
```

`credentials.yml`
Configure your credentials.yml file if you're integrating with external channels like Slack, Facebook Messenger, etc.

## Running the Bot

### Start the Action Server

Run the following command in a separate terminal to start the action server:

```bash
rasa run actions
```

## Train the Model

Before you can chat with your bot, you need to train it:

```bash
rasa train
```

## Start Rasa Server

In a new terminal, start the Rasa server:

```bash
rasa shell
```

## Usage

Once the Rasa server is running, you can start chatting with the bot in the terminal.

## Custom Actions

The actions.py file contains the custom actions used for negotiating prices. Ensure that this file is properly maintained and updated as per your negotiation logic.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

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