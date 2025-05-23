REQUEST
Problem: This is a README file from a Rasa chatbot repository # rasaFinancial

## How to test ?

- `pip install -r requirements.txt`: Install requirements.
- `rasa train`: Train your Rasa model using your configured pipeline and data.
- `rasa shell`: Test your trained model in the command-line shell as well as interact with your model via Flask.
- `rasa run actions`: Run custom actions defined in actions.py alongside your Rasa server.
- run `python app.py` with Flask's built-in server.
- run `python automation_script.py` to run all other scripts that interact with the running Flask server.
- Set up PostgreSQL & PgAdmin4, then from the query tool run these queries:
- `CREATE USER username WITH PASSWORD 'password';`
- `CREATE DATABASE db_name;`
- `GRANT ALL PRIVILEGES ON DATABASE db_name TO username;`
- `GRANT ALL PRIVILEGES ON SCHEMA public TO username;`
- To connect to Database from Flask app:
- `flask db init`
- `flask db migrate -m "Initial migration"`
- `flask db upgrade`
- To check if Database is connected:
- `SELECT * FROM "user";`
- `SELECT * FROM "reported_conversations";`

## .env file format

- `ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key`
- `DB_USERNAME=username`
- `DB_PASSWORD=password`
- `DB_NAME=db_name`
- `SECRET_KEY=your_secret_key` get your secret key using this command `print(os.urandom(24))`
- `MAIL_USERNAME=your_project_email_id`
- `MAIL_PASSWORD=your_google_app_password` to get this, create a google app.
- `ROOT_DIRECTORY=path_to_your_root_directory` for LOC Counter.
- `EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key` for currency conversion.

## General Commands

- `rasa init`: Initialize a new Rasa project.
- `rasa run`: Run the Rasa server to interact with your model via REST API.
- `rasa run --enable-api`: Run the Rasa server with HTTP API enabled.
- `docker ps`: List all active Docker containers.
- `docker kill [container_name]`: Kill a specific Docker container.
- `rasa train nlu`: Train the NLU (Natural Language Understanding) model only, focusing on intents.
- `rasa shell nlu`: Test the NLU model by checking intent confidence scores for a given query.
- `rasa shell -m models\older-model-name`: To run an older model.
- `rasa data validate`: Validate your domain, NLU, and story data for any conflicts or inconsistencies.
- `rasa test`: Run tests on your Rasa model and evaluate the results.

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    PostgreSQL, Alpha Vantage, Exchange Rate API, Google App,,##
PostgreSQL PgAdmin4 Alpha Vantage Exchange Rate API,,##
PostgreSQL, Alpha Vantage, Exchange Rate API, Google App,,##
PostgreSQL, Alpha Vantage, Exchange Rate API, Google App,,##
PostgreSQL PgAdmin4 Alpha Vantage Exchange Rate API Google App,,##
PostgreSQL, PgAdmin4, Alpha Vantage, Google App, Exchange Rate API,,##
PostgreSQL, Alpha Vantage, Exchange Rate API, Google App,,##
PostgreSQL, Alpha Vantage, Exchange Rate API, Google App,,##
PostgreSQL, PgAdmin4, Alpha Vantage, Exchange Rate API, Google App,,##
PostgreSQL PgAdmin4 Alpha Vantage Exchange Rate API,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
PostgreSQL, Alpha Vantage, Exchange Rate API, Google App

## Purpose of external services

- **PostgreSQL**: A relational database used to store user data and reported conversations.
- **Alpha Vantage**: A service providing real-time and historical stock market data.
- **Exchange Rate API**: A service used for currency conversion.
- **Google App**: Used for sending emails via a Google account.