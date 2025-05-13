REQUEST
Problem: This is a README file from a Rasa chatbot repository # JobSearch Wizard 🧙‍♂️💼

Welcome to **JobSearch Wizard**, your ultimate tool for effortlessly finding your dream job! 🚀✨

## What It Does 🌟

**JobSearch Wizard** is a powerful web scraping tool that scours the web for job listings across various platforms. 🕵️‍♀️🔍 It leverages cutting-edge technology to gather and present job opportunities tailored to your preferences.

## Features 🛠️

- **Web Scraping**: Extracts job listings from multiple job sites with precision. 🧹💻
- **Streamlit Dashboard**: User-friendly and interactive interface to display job results. 📊📈
- **Rasa Chatbot**: Conversational AI that understands your job title and location preferences. 🤖💬
- **Customizable Filters**: Fine-tune your search with specific criteria for a more targeted job search. 🎯🔧

## How It Works 🔄

1. **Interact with the Rasa Chatbot**: Share your desired job title and location. 🗣️📍
2. **Search Across Multiple Sites**: Our backend scrapes relevant job listings from top job boards. 🌐🔎
3. **View Results on Streamlit**: Easily browse through a clean and organized dashboard to find your ideal job. 🖥️📋

## Getting Started 🚀

1. Clone the repository: `git clone https://github.com/RakeshYads/Job_Search.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

For detailed instructions, check out our [documentation](link-to-docs).

## Contribute 🤝

We welcome contributions from the community! Feel free to submit issues, feature requests, or pull requests. Let's build the ultimate job search tool together! 🌟💪

---

Ready to revolutionize your job search? Let **JobSearch Wizard** be your guide to finding the perfect opportunity! 🌟🔍💼

**Happy Job Hunting!** 🕵️‍♂️✨

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: Rasa, Streamlit, Web scraping,,##
Rasa, Streamlit,,##
Rasa,,##
Databases and services: Rasa, Streamlit,,##
Databases and services: Rasa, Streamlit
Databases and services: Rasa, Streamlit,,##
Rasa, Streamlit,,##
Databases and services: Rasa, Streamlit
Databases and services: Rasa, Streamlit
Rasa, Streamlit,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Rasa, Streamlit

## Purpose of external services

- **Rasa**: Rasa is used as the conversational AI platform to build and manage the chatbot that interacts with users to understand their job title and location preferences.
- **Streamlit**: Streamlit is used to create a user-friendly and interactive dashboard to display the job search results gathered by the web scraping tool.