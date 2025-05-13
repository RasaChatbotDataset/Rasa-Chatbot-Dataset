REQUEST
Problem: This is a README file from a Rasa chatbot repository # 🌟 Welcome to Our Chatbot Repository! 🌟


### Executing Career Advisor Chatbot
🤖 Here are the instructions to run it in the terminal.

# Open your Windows PowerShell or Terminal and execute:
   
 Step 1: Create a new directory called 'careerAdvisor' to organize project-related files.
```bash
mkdir careerAdvisor
 ```
 Step 2: Change the current working directory to the newly created 'careerAdvisor' directory.
```bash
cd careerAdvisor
 ```
 Step 3: Clone the repository from GitHub. This command fetches the project files from the provided URL.
```bash
git clone https://github.com/Carlosjr5/Career-Advisor-Bot.git
 ```
 Step 4: Change the directory to 'Career-Advisor-Bot', which is expected to be a directory inside the cloned repository.
```bash
cd Career-Advisor-Bot
 ```
 Step 5: Start a new instance of the bash shell in the root. This command is typically not necessary in a script unless for specific reasons, like running a script that needs bash-specific features.
```bash
bash
 ```
 Step 6: Create a Python virtual environment in the current directory inside a folder named 'venv'. This environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.You might need to use 'py' instead of 'python3' depends on your python version installed.
```bash
python3 -m venv ./venv
 ```
 Step 7: Activate the previously created virtual environment. This modifies the current shell environment to use the python and pip commands from the virtual environment, rather than any globally installed versions.
```bash
source ./venv/bin/activate
 ```
 Step 8: Use pip to install Rasa, which is an open source machine learning framework to automate text- and voice-based conversations.
```bash
pip install rasa
 ```
 Step 9: Start the Rasa action server, which allows you to run custom actions for details in conversations that cannot be handled in the Rasa dialog manager alone. IF GETTING AN ISSUE OF ModuleNotFoundError: No module named 'pandas' JUST DO 'pip install pandas' then 'rasa run actions'.
 ```bash
pip install pandas
 ```
```bash
rasa run actions
 ```
 Step 10: OPEN A NEW TERMINAL WINDOW ON CURRENT WORKING FOLDER(Career-Advisor-Bot), RUN THE STEP 5 & 7 and continue with Train a new Rasa model using the training data. The trained model will be used to make predictions about user inputs.
```bash
rasa train
 ```
 Step 11: Whenever the model is trained you can  Start the main Rasa server and enable the API. This allows Rasa to handle user messages via HTTP requests.
  ```bash
rasa run --enable-api
 ```
 Step 12: OPEN A NEW TERMINAL WINDOW ON CURRENT WORKING FOLDER(Career-Advisor-Bot), RUN THE STEP 5 & 7 and Run the Streamlit application named 'app.py'. Streamlit is an open-source app framework for Machine Learning and Data Science projects.
  ```bash
pip install streamlit
  ```
  ```bash
streamlit run app.py
  ```

This will launch the career advisor chatbot user interface, allowing you to start chatting instantly! 🗣️💬

<img width="677" alt="image" src="https://github.com/Carlosjr5/Career-Advisor-Bot/assets/77840319/df3e71c6-859c-4c6d-8ea2-5a043872cb78">


Happy coding! If you have any questions or ideas, feel free to reach out. Let's make this chatbot project an epic adventure! 🤖


**Carlos Jiménez Rodríguez**  
  📧 cjimenezr23@gmail.com

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    None
None
None
Databases and services: pandas, Rasa, Streamlit,,###
Databases and services: pandas, Streamlit,,###
None
None
None
Databases and services: pandas, Streamlit,,###
pandas,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
pandas, Rasa, Streamlit

### Purpose of external services
- **pandas**: Used for data manipulation and analysis, particularly for handling structured data in the form of dataframes.
- **Rasa**: An open-source machine learning framework for building conversational AI, including chatbots.
- **Streamlit**: An open-source app framework used to create and share custom web apps for machine learning and data science projects.