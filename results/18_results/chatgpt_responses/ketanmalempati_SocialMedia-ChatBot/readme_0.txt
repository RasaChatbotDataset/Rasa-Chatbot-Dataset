REQUEST
Problem: This is a README file from a Rasa chatbot repository # CMPE-252 SocialMedia-ChatBot
One stop solution to all social media.

## Motivation
We spend lot of time using social media and potentially waste our time. Even though we might have to search something important we tend to get deviated. So this chatbot will send results of only the things you wanted to search and not waste much time.  

## How to run
- First install rasa on your system using `pip install rasa`
- Then run `rasa init` to create an initial model
- You can start changing all the files present in the folder
- Run `rasa train` after ever change made before running
- After training run `rasa shell` or `rasa interactive` if you want to run in terminal
- Use `rasa run` if you have connected it to slack and you can start the conversation in slack
- In a new terminal run `rasa run actions` so you can connect to APIs  
## Conversation Flows
- **Single Conversations**
 1. - **User Input** : Virat Kohli
    - **Bot Reply** : He is the G.O.A.T  
    - **Bot Reply** : *Also adds an image of him*  
 2. - **User Input** : What time is it?
    - **Bot Reply** : `current time`
 3. - **User Input** : Can I get some details on football?
    - **Bot Reply** : Here are the recent tweets and videos on football  
    - **Bot Reply** : *3 tweets and 3 video links on football*  


- **Multi-turn Conversations**
 1. - **User Input** : Can I have details on Elon musk?
    - **Bot Reply** : Recent Tweets and videos on Elon Musk: *Attaches 3 tweets and 3 videos on Elon Musk*
    - **Bot Reply** : Here are the things related to Elon Musk (1) SpaceX (2) Tesla
    - **User Input** : SpaceX
    - **Bot Reply** : Recent Tweets and videos on SpaceX: *Attaches 3 tweets and 3 videos on SpaceX*
 2. - **User Input** : Details on Sports?
    - **Bot Reply** : Recent Tweets and videos on Sports: *Attaches 3 tweets and 3 videos on sports*
    - **Bot Reply** : Here are the things related to Sports (1) Football (2) Tennis
    - **User Input** : Tennis
    - **Bot Reply** : Recent Tweets and videos on Tennis: *Attaches 3 tweets and 3 videos on Tennis*
 3. - **User Input** : About Tim Cook?
    - **Bot Reply** : Recent Tweets and videos on Tim Cook: *Attaches 3 tweets and 3 videos on Tim Cook*
    - **Bot Reply** : Here are the things related to Tim Cook (1) Iphone (2) MacBook
    - **User Input** : Details on Iphone
    - **Bot Reply** : Recent Tweets and videos on Iphone: *Attaches 3 tweets and 3 videos on Iphone*
 4. - **User Input** : Can I have details on Artificial Intelligence?
    - **Bot Reply** : Recent Tweets and videos on Artificial Intelligence: *Attaches 3 tweets and 3 videos on Artificial Intelligence*
    - **Bot Reply** : Here are the things related to Artificial Intelligence (1) NLP (2) CV
    - **User Input** : CV
    - **Bot Reply** : Recent Tweets and videos on CV: *Attaches 3 tweets and 3 videos on CV*  

- **Slots Filling Conversation**
 1. - **User Input** : I want 3 videos on Nature
    - **Bot Reply** : I will now send posts for you!
    - **Bot Reply** : I will send 3 videos post on nature.
    - **Bot Reply** : *Adds 3 video links on nature*
 2. - **User Input** : I want 5 tweets on England
    - **Bot Reply** : I will now send posts for you!
    - **Bot Reply** : I will send 5 videos post on England.
    - **Bot Reply** : *Adds 5 tweet links on England*
 3. - **User Input** : I want tweets
    - **Bot Reply** : OK! You want to have posts from tweets.      
    - **Bot Reply** : How many posts do you want?  
    - **User Input** : I want 7
    - **Bot Reply** : OK! You want to have a 7 posts.
    - **Bot Reply** : On what topic would you like to see?
    - **User Input** : I want posts on Beaches
    - **Bot Reply** : I will send 7 tweets on Beaches
    - **Bot Reply** : *Adds 7 tweet links on Beaches*  

- **Database usage Conversations**
 1. - **User Input** : Show me my search history
    - **Bot Reply** : Sending your search history *(It will display the search history by pulling data from database)*
 2. - **User Input** : Delete my search history
    - **Bot Reply** : Deleting your search history *(It will delete the search history from the table in the database)*  

## Future Improvements
- Make it more generic to detect Proper Noun better.
- Add more social media platforms.
- Add Translations to other languages.
- Add Feedback Form.
## Challenges faced
- Named Entity detection was difficult.
- Trying to run actions for the first time was very difficult as I made made mistakes in port number.
- Adding the bot to slack for a little tedious process.
## Conclusion
This project pulls a number of posts of the topics you specify from the social media platforms you choose or all available.  
This saves time by avoiding switching from one social media platform to another and becoming distracted in the process.  
I learned a lot of things, such as how to build a conservational AI chatbot and how to manage my time.  
During class and office hours, I was able to learn a lot from the ISAs.  
Overall, it was an enjoyable project to work on.  
## References
- https://rasa.com/docs/rasa/installation/environment-set-up/
- https://www.youtube.com/watch?v=2Qu4LCvB4bs&t=456s
- https://github.com/RasaHQ/rasa-3.x-form-examples
- https://www.youtube.com/watch?v=VcbfcsjBBIg&t=630s
- https://www.youtube.com/watch?v=hIWnpyTWsLQ&t=1096s
- https://www.youtube.com/watch?v=Ds8cB3LZwfU&t=799s
- https://rasa.com/
- https://github.com/RasaHQ/rasa-2.x-form-examples

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: Slack, Twitter, YouTube,,##
Databases and services: Slack, Twitter, YouTube,,##
Slack, Database,,##
Slack, Database,,##
Databases and services: Slack, Twitter, YouTube,,##
Slack,,##
Databases and services: Slack, Twitter, YouTube,,##
Databases and services: Slack, Twitter, YouTube,,##
Databases and services: Slack, Twitter, YouTube,,##
Slack,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Slack, Twitter, YouTube, Database

## Purpose of external services
- **Slack**: Used to connect the chatbot to Slack for conversations.
- **Twitter**: Used to fetch recent tweets based on user queries.
- **YouTube**: Used to fetch video links based on user queries.
- **Database**: Used to store and retrieve user search history.