REQUEST
Problem: This is a README file from a Rasa chatbot repository # Chatbot Countries
## Introduction
Using [Rasa 3.0](https://rasa.com/docs/rasa/) to create a customized, and user friendly AI bot that can help with countries.
you can ask things like:
- Show me countries around the world.
- What do you know about Greece?
- what is the population of Australia?
- Tell me the capital of Japan.

It can Handle different stories, variations, and case sensitive words.
example:
<pre>
<b>Input:</b> Tell me the capital of USA.
<b>Bot:</b> Washington, D.C. is the capital of USA.
<b>Input:</b> what about its population?
<b>Bot:</b> There is 32.82 crores in USA.
</pre>
## Run chatbot
To run chatbot on your system you need to install rasa 3.0 on your virtual environment (anaconda)
following this link to install rasa on your local drive: [youtube](https://www.youtube.com/watch?v=GlR60CvTh8A) or [Rasa documentation](https://rasa.com/docs/rasa/installation)

after installation:
1. Open your conda virtual env for rasa in terminal.
2. Clone this repo to your project directory
3. Open the first terminal, and run:
    - **`rasa train`**
4. Open new terminal with rasa virtual env to run actions server, make sure you are in the project directory, and run: 
    - **`rasa run actions`**
5. Get back to the first terminal, and run:
    - **`rasa shell`**
6. From here you are good to go with the chatbot. **Have fun ^_^**

Note: for a more interactive way, and to get to share chatbot link over the network see [rasa x](https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide).

## Bot example
Here is an example for a conversation driven through different turns.

<img src="https://github.com/hazemhosny/Chatbot_Countries/blob/main/BotExample.png" alt="BotExample" width="850"/>

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