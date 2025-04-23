REQUEST
Problem: This is a README file from a Rasa chatbot repository # 📚 Overview

💬 RasaScribe is the go-to script generating chatbot platform built on top of [Rasa](https://github.com/RasaHQ/rasa) and Gemini API. It provides you with scripts, captions and hashtags of any topic that you wish. If you dont have any specific topics, no worries! The chatbot will search the web for all the trending topics for your specified domain! 👀

## 📖 What is Rasa?

In their own words:

>💬 Rasa is an open source (Python) machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants

<br/><br/>

## 📝 Why RasaScribe?

- RasaScribe works out of the box. It has the ability to generate latest trending topics in any domain.
- Is a closed-form chatbot and there's no problem of hallucination since it works mostly on NLU.
- A quick-to-use tool, where just entering three keywords generates an entire scipt.
- Can generate captions and hashtags depending on the platform you are using.
- Extracts the information the users have entered, which can then be used to retrain the rasa chatbot.

<br/>

## 🤓☝️ How does it work?

- Uses NLU to understand if you have an idea for your post or not.
- If you dont have an idea, it uses top treading youtube videos in your specified domain.
- It scrapes the transcripts and passes it to Gemini API
- This API returns the scripts, captions and hashtags considering your specified platform.
- Here's a flowchart of how RasaScribe works :

![final contentGenerator](https://github.com/user-attachments/assets/423759b8-e6ea-4f2e-8a03-ca87b0b6cf6e)

<br/>

## 🎬 Demo Video

https://github.com/user-attachments/assets/bacd448c-6047-4ab9-854a-abe8c9a5fc0c

<br/>

# 🧑‍💻 Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/AkshayKulkarni3467/RasaScribe.git
    ```
2. Navigate to the project directory:
    ```sh
    cd RasaScribe
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

# ✨ Quick Start
1. Get a gemini api key and set it as an environment variable with name 'GOOGLE_API_KEY' 
2. Get a youtube data v3 api key and set it as an environment variable with name 'YOUTUBE_API_KEY'
3. Replace `os.getenv['SQL_PW']` with your local database password in actions.py 
4. To set up a whatsapp testing sandbox, host your chatbot with ngrok and setup and account on twilio.
5. Get the sid, auth_token and whatsapp number and copy it to credentials.yml
6. In your cmd, type:
    ```sh
    rasa run actions
    ```
    ```sh
    python callback_server.py
    ```
    ```sh
    rasa run
    ```

## ✏️ Tuning for retriving proper topics

In the actions.py file, you can modify the following parameters to generate better results

1. Modify the no of years parameter (Checks if the searched result is published after the specified no of years):
    ```python
    response = self.get_yt_video_ids(response,no_of_years=3)
    ```
2. Modify the max results to generated more context for a give topic:
    ```python
    response = self.youtube_search(query_string,maxResults=25)
    ```
3. Modify the indexs slicing to generate a much longet transcript:
    ```python
    return youtube_id_list[:5]
    ```

## 🌟 Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch`
5. Open a pull request.

## 🔎 Future Plans
- Adding audio suggestions for short form videos content.
- Adding a functionality of two stage fallback.
- Adding a functionality of posting image links and generating script based on that image.

## 📜 License
This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🛠️ Acknowledgements
- Inspired by the hype of gen ai to come out and develop my own tools.
- Special thanks to the contributors and the open-source community.

## 📞 Contact
For more information, visit the [Project](https://github.com/AkshayKulkarni3467/RasaScribe).

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: local database, Gemini API, YouTube Data v3 API, Twilio,,##
Local database, Gemini API, YouTube Data v3 API, Twilio,,##
Databases and services: Gemini API, YouTube Data v3 API, local database, Twilio,,##
Databases and services: Gemini API, YouTube Data v3 API, Twilio, local database,,##
Databases and services: Gemini API, YouTube Data v3 API, Twilio, local database,,##
Local database, Gemini API, YouTube Data v3 API, Twilio,,##
Databases and services: Gemini API, YouTube Data v3 API, Twilio, local database,,##
Databases and services: Gemini API, YouTube Data v3 API, Twilio, local database,,##
Databases and services: local database, Gemini API, YouTube Data v3 API, Twilio,,##
Databases and services: Gemini API, YouTube Data v3 API, Twilio, local database,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Gemini API, YouTube Data v3 API, Twilio, local database

## Purpose of external services
- **Gemini API**: Used to generate scripts, captions, and hashtags based on the provided transcripts.
- **YouTube Data v3 API**: Used to fetch trending YouTube videos and their transcripts in the specified domain.
- **Twilio**: Used to set up a WhatsApp testing sandbox for hosting the chatbot.
- **Local database**: Used to store and retrieve user information for retraining the Rasa chatbot.