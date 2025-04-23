REQUEST
Problem: This is a README file from a Rasa chatbot repository # Conversational_AI--Healthcare-VoiceBot
# Introduction
" Dataset for training an NLU model to provide healthcare assistance. "

The dataset is in the format specified by the requirements of RASA framework as the model is tested and deployed using the same.

# RASA Setup
<ul>
  <li>Clone/ Download the repo</li>
  <li>Create an env for installing rasa</li>
  <ul>
    <li>We use conda to create the virtual environment, open your preferred command line/terminal/shell in the extracted directory and all the commands are to be performed here</li>
    <li>Execute <code>conda create --prefix ./env_name python=3.6</code> to create an env in the same directory</li>
  </ul>
  <li>If conda is not installed</li>
  <ul>
    <li>Install it from <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html">Here</a></li>
    <li>or use python venv (or) any other env manager, <a href="https://rasa.com/docs/rasa/installation/">guide</a></li>
  </ul>
  <li>Activate the env using  <code>conda activate ./env_name </code></li>
  <li>Install the dependencies</li>
  <ul><li> <code>pip install rasa </code></li></ul>
</ul>
<blockquote>
<p dir="auto">" Note: The env creation is optional and can also be performed directly in the base env but it is recommended to create a new env as the dependencies are large and might effect the storage/performance if directly installed"</p>
</blockquote>
<h2>VoiceBot Commands</h2>
<p dir="auto">Step 1: Speech to Text</p>
<p dir="auto">------ pip install SpeechRecognition PyAudio</p>
<p dir="auto">Step 2: Externally sending an input to rasa chatbot</p>
<p dir="auto">------ rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml</p>
<p dir="auto">Step 3: Text to speech conversion</p>
<p dir="auto">------ pip install gtts and also install the media player for playing the audio after conversion,</p>
<p dir="auto">set any media player path to the project Now to see your voice bot in action run the Voice.py file and also run the action server using</p>
<p dir="auto">------ rasa run actions</p>
<p dir="auto">At last run the voicebot python file</p>
</article>

# Usage

<ul dir="auto">
<li>Open the directory and activate the env from comman line.</li>
<li>Train the model using <code> rasa train </code> this creates a model in the models directory.</li>
<li>Run the model : <code> rasa shell </code>.</li>
<li>The trained AI chatbot model will be now active</li>
</ul>

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