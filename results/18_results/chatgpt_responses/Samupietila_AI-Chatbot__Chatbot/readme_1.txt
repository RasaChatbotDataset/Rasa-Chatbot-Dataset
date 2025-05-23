REQUEST
Problem: This is a README file from a Rasa chatbot repository ## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-Run-the-Project)
- [Contributing](#Contributing)
- [License](#License)
- [Contributors](#contributors)

## Introduction

# Essi-bot - Interactive Quiz bot

This project is designed to create an interactive quiz bot using Rasa, intended for customer service purposes. It supports users by answering queries.

- **Responding to queries**
- **Record user interactions in a MySQL database**

## Technologies Used

### Main Technologies

- **Rasa**: An open-source framework for building conversational AI.

- **Flask**: A micro web framework used to serve the Rasa model and handle API requests.

- **MySQL**: A relational database for user data storage and authentication.

### Frontend Technologies

- **HTML/CSS:** For structuring and styling the user interface.
- **JavaScript**: To manage interactions within the chat interface.

### Python Libraries

- **Mysql-connector-python**: To connect to the MySQL database.
- **Flask-Cors**: To handle cross-origin resource sharing for API requests.

### Development Tools

- **Visual Studio Code**: Code editor for development.
- **Pycharm**: Code editor for development.
- **Postman**: For testing API endpoints.
- **MySQL Workbench:** For database management.

### AI-Tools used

- **ChatGPT**

## Features

### Chatbot Functionality

- Handles service inquiries.
- Provides responses based on user input.

### Database Integration:

- Records timestamp from start of the chat.
- Returns localized welcome message after registration based on the selected language of the page.
- Saves user information about registered users.

### Visualization:

- An HTML page visualizes the Rasa Core conversation flow.

## How to Run the Project

### Prerequisites

- Python 3.x installed on your machine.
- MySQL Server set up and running.
- Node.js installed.

### Setup Instructions

1. **Clone the Repository:**

```
git config --global http.postBuffer 524288000
git clone https://github.com/Samupietila/AI-Chatbot.git
```

cd repository-folder

2. **Install Required Packages:** Create a virtual environment and activate it:

# For Mac/Linux

```
source venv/bin/activate

python3 -m venv venv
```

# For Windows

```
python -m venv venv
venv\Scripts\activate
```

**Install the required Python packages**:

```
pip install -r Chatbot/requirements.txt
pip install -r Flask-Website/requirements.txt
```

3. **Configure Database Settings:** Create the Flask-Website/Database/config.py file with your MySQL credentials.
```
DB_CONFIG = {
'user': 'yourdatabaseuser',
'password': 'yourdatabasepassword',
'host': 'localhost',
'database': 'ChatAppDatabase',
'charset': 'utf8mb4',
'collation': 'utf8mb4_unicode_ci',
'raise_on_warnings': True
}
```




4. **Set Up the Database**: Run the SQL scripts provided in **Flask-Website/Database/database.sql** to create the necessary tables in your MySQL database.

5. **First terminal to train and run rasa:**
   From your project root folder go to "Chatbot"-folder:

   ```
   cd Chatbot
   rasa train
   ```

### After successfully trained new rasa model

   ```
   rasa run
```

6. **Second terminal to run rasa actions:**
   ```
   cd Chatbot
   rasa run actions
   ```

7. **Third terminal to run Flask server:**
   ```
   cd Flask-Website
   python main.py
   ```

9. **Interact with the Chatbot:**
   Access the chatbot via the web interface from the link that Flask server gives.
   e.g. "Running on http://127.0.0.1:5000"

**Check TroubleShootingGuide.md from Documents if you run to any problems during installation**

## How to use Essi-bot

1. **Open the bot-window from chatbot icon at the sites right bottom corner**
2. **Greet the bot by sending a message to it** e.g. "Hello"
3. **The bot asks what you need help with**
4. **User will choose the subject and the bot will answer**

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.  
You can view the full license [here](https://creativecommons.org/licenses/by-nc/4.0/).

## Contributors

Samu, Mika, Samuel, Zehra, Jukka

## Ohjelmistotuotantoprojekti

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    MySQL,,##
MySQL, ChatGPT,,##
MySQL,,##
MySQL,,##
MySQL, ChatGPT,,##
MySQL, ChatGPT,,##
MySQL, ChatGPT,,##
MySQL, ChatGPT,,##
MySQL,,##
MySQL, ChatGPT,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
MySQL, ChatGPT

## Purpose of external services

- **MySQL**: Used as a relational database for storing user data, interactions, and authentication information.
- **ChatGPT**: Utilized for generating conversational responses and enhancing the chatbot's ability to understand and respond to user queries.