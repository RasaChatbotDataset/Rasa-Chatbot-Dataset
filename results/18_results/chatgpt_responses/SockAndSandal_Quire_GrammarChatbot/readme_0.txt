REQUEST
Problem: This is a README file from a Rasa chatbot repository # Quire - A Chatbot that's built to point out your mistakes. Gramatically.

##### _This chatbot is made on Rasa 3.0, so please make sure you have Rasa 3.0 installed on the env for proper functioning of this chatbot._

## Steps for Installation
1. Clone this repo into a folder of your choosing.
2. Make sure you have **Python** (`brew install python`), **Rasa** (`pip install rasa==3.0`), and **Tensorflow** installed (`pip install tensorflow`)
3. Alternatively, you can also use the requirements folder in the repo to install everything you need.
4. Navigate (`cd`) to the cloned repository.
5. You'll need to supply an API key for [WordsAPI](https://rapidapi.com/dpventures/api/wordsapi). Do this by making a config.py file inside the actions folder, then declaring a variable `api_key` inside this file.
6. Start the action server with `rasa run actions` and leave this running in a terminal window.
7. Open a new terminal window and run `rasa shell`. If a model isn't trained, run `rasa train` first.

Note: If installing Rasa 3.0 gives you dependency errors, Rasa 3.1 or 3.2 will also work for running this chatbot.

## Suggested Conversation Flows

### Ask Quire to tell you to use a word in a sentence.
  You: Hi \
  **Quire**: Hi! How can I help you? \
  **You**: Use the word angry in a sentence \
  **Quire**: They were angry because their plans had been discovered \
  **Quire**: Was that helpful? \
  **You**: No \
  **Quire**: She gave her companion an angry glance. \
  **Quire**: Was that helpful? \
  **You**: Yes \
  **Quire**: Great!

### Ask Quire to tell you the meaning of a word.
  **You**: What does umbrella mean? \
  **Quire**: Umbrella(noun): a device consisting of a circular canopy of cloth on a folding metal frame supported by a central rod, used as protection against rain or sometimes sun. 

### Ask Quire to tell you to rhyming words for a word.
  **You**: Give me rhyming words for old. \
  **Quire**: old rhymes with cold, fourfold, and sheepfold
######  _(They're a little odd for rhymes, but that's got more to do with the API it is pulling from than Quire itself.)_

### Ask Quire to tell you to opposite words for a word.
  **You**: What is the opposite of brother? \
  **Quire**: brother x sister 

### BONUS: Ask Quire to tell you a joke. Or tell it your name, it will remember. You could also ask Quire why it is named that and it will tell you.


### Current Issues:

1. Quire doesn't take very well to typos in the words themselves. It might understand when you say "what is the oposite of brother" but is much less likely to understand or give you the right response if you spell "brother" wrong. This has got to do with the fact that the words are the literal queries that feed as input to our API and the API doesn't take very well to typos.
2. While Quire is good at slot mapping for a large variety of words, whether that is for meanings of words or using in sentences, it can fail at mapping the correct word to the slots when it encounters words that are very different from what it's been trained for. While it is easy to mitigate this issue using a form format where I turn this into a multi-turn conversation and ask to input the word in a different sentence, I don't think that is a natural way to interact with a chatbot in the real world. 

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    WordsAPI,,##
WordsAPI,,##
WordsAPI,,##
WordsAPI,,##
WordsAPI,,##
WordsAPI,,##
WordsAPI,,##
WordsAPI,,##
WordsAPI,,##
WordsAPI,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
WordsAPI

## Purpose of external services
**WordsAPI**: This service is used to provide definitions, example sentences, rhyming words, and antonyms for the words queried by the user.