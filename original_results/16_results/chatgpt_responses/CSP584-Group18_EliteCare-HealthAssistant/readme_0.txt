REQUEST
Problem: This is a README file from a Rasa chatbot repository 
# EliteCare - Health Assistant
Overview: EliteCare is an enterprise-level web application designed for the healthcare sector, focusing on online pharmacy services. The primary goal of this project is to streamline the customer experience in selecting and understanding medications by integrating an AI-powered virtual assistant. This assistant helps users with real-time answers to their medication queries, personalized product recommendations, dosage guidance, and potential side-effect checks.

The application leverages RASA AI to handle natural language understanding (NLU) and dialogue management, allowing the system to engage with users in a conversational manner. By analyzing symptoms and preferences, the chatbot can recommend suitable medications and help users navigate through a large variety of pharmaceutical products.

Key Features:

Medication Inquiry Support: Assisting customers with instant suggestions for medications based on symptoms.
Personalized Recommendations: Offering products tailored to user needs, enhancing the overall shopping experience.
Drug Interaction & Side Effect Checks: Providing critical information regarding medication safety.
RASA AI Integration: RASA’s open-source framework plays a central role in the AI functionalities of EliteCare, enabling both natural language understanding and personalized dialogue flow. The system is configured using several key components:

NLU to extract intents (e.g., medication inquiries) and entities (e.g., drug names or dosage).
Rules and Stories to manage the conversational flow, ensuring users receive the right information at the right time.
Domain & Actions to define the scope of the AI’s responses and custom logic for the recommendations.
This setup allows the assistant to continuously learn from interactions, improving its efficiency and accuracy in providing healthcare advice over time.


---

**Technologies Used**

- **Server Side**: Express.js
- **Frontend**: React.js, Axios
- **Database**: MongoDB
- **AI Platform**: Rasa (Python)
- **Other Libraries**: Axios (for HTTP requests)

---

## Project Structure

```
/backend   # Node.js Express server code
/database  # MongoDB setup and configuration
/frontend  # React.js client-side application
/rasa      # Rasa AI Agent (NLP and machine learning models)
```

---

## Getting Started

To get started with the project, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/CSP584-Group18/Health-Assistant.git
cd Health-Assistant
```

### 2. Backend Setup

1. Install **Visual Studio Code**: Download and install from [here](https://code.visualstudio.com/).
2. Install **Node.js** and **npm**: Download and install from [Node.js Official Site](https://nodejs.org/en).

#### Start the Node Backend:

- Navigate to the `/backend` directory:
  ```bash
  cd /backend
  ```

- Install backend dependencies:
  ```bash
  npm install
  ```

- Start the backend server:
  ```bash
  node server.js
  ```

---

### 3. Frontend Setup

1. Ensure **npm** is installed (as in the backend setup).

#### Start the React Frontend:

- Navigate to the `/frontend` directory:
  ```bash
  cd /frontend
  ```

- Install frontend dependencies:
  ```bash
  npm install
  ```
  or if fails
  ```bash
  npm install --legacy-peer-deps
  ```

- Start the client-side React application:
  ```bash
  npm start
  ```

- The app should now be running at `http://localhost:3000`.

---

### 4. AI (Rasa) Setup

1. Ensure you have Rasa installed (requires Python environment).

#### Start the Rasa AI Agent:

- Navigate to the `/rasa` directory:
  ```bash
  cd /rasa
  ```

- Train the Rasa model:
  ```bash
  rasa train
  ```

- Run Rasa actions:
  ```bash
  rasa run actions
  ```

- Start the Rasa server:
  ```bash
  rasa run --cors "*"   
  ```

---

## Additional Notes

- Ensure that **MongoDB** is properly set up and running before starting the backend.
- The project relies on several third-party APIs; make sure to configure any required API keys in `.env` files as per the needs of your application.
  
---

Feel free to adjust any paths or commands according to your development environment.

---

## Contributors

- [Dhruv Patel](https://github.com/dhruvpatel77741)  
- [Dirgh Patel](https://github.com/dirghpatel3110)  
- [Sakshi Patel](https://github.com/sakshipatel29)  
- [Dhruvi Patel](https://github.com/dhruvipatel-24)  

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    MongoDB, Rasa, Axios,,---,,##
MongoDB, Rasa, Axios,,##
MongoDB, Rasa, Axios,,##
MongoDB, several third-party APIs,,##
MongoDB, Rasa, Axios,,---,,##
MongoDB, Rasa, Axios,,##
MongoDB, third-party APIs,,##
MongoDB, third-party APIs,,##
MongoDB, Rasa, Axios,,---,,##
MongoDB, Rasa, Axios,,---,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
MongoDB, Rasa, third-party APIs

## Purpose of external services

- **MongoDB**: Used as the database to store and manage data related to the application, such as user information, medication details, and interaction logs.
- **Rasa**: An open-source AI platform used for natural language understanding (NLU) and dialogue management, enabling the chatbot to understand and respond to user queries.
- **Third-party APIs**: Used to fetch additional data or services required by the application, such as drug information, side effects, and interactions.