REQUEST
Problem: This is a README file from a Rasa chatbot repository # shoestorechatbot
--Setup
This chatbot is made to run on Windows CMD command line
To run this chatbot on Windows 10 you need to follow these steps in this video.
https://www.youtube.com/watch?v=GlR60CvTh8A.
Afterwards you need to install Spacy using the command "pip install spacy"
Then type in the command "pip install spacy-transformers"
Afterwards you need to install a Spacy pretrained model using the command "python -m spacy download en_core_web_md"

--launch
After setting up your environment all you need to do is go into the project directory in your CMD command line and type "rasa train"
After the training is done loading, you need to open a second CMD command line.
In the first command line run the command "rasa run actions".
In the second command line run "rasa shell". 
You can now interact with the bot in the second command line.

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