REQUEST
Problem: This is a README file from a Rasa chatbot repository # A-Question-Answering-Approach-for-Cognitive-Understanding-of-A-5-Axis-Articulated-Robot-Control

This is my undergraduate Final Year Project.

**Note that the movement control code in the repository is adjusted to my prototype due to several hardware limitations on the robotic arm such as the imprecise angle of the robotic arm frame due to the weight of the servo motor. Hence, the accuracy of the robotic arm in successfully locating its end effector to the desired coordinate varies, and some adjustments on the code would be needed to the movement control and working envelope.**

### Overview:
This project focuses on making a robotic arm to be a personal assistant. The concept is to develop a cognitive understanding for the robotic arm to understand the users intent through their commands, which can be an abstract or direct commands. From the commands, the robotic arm will execute the desired programmed actions to assist the user. It utilizes four different field of AI implementation: Artificial Neural Network, Speech Recognition, Natural Language Processing, and Computer Vision. A prototype is build with the aforementioned implementation with some Robotic Engineering to showcase the use case of the project.

### Prototype:
<img align="right" width="470" src="https://github.com/BradLoo51/A-Question-Answering-Approach-for-Cognitive-Understanding-of-A-5-Axis-Articulated-Robot-Control/assets/172585249/04cdede4-bc60-47fc-8b1c-ca6aec617ad4"/>

Materials used:
- Arduino UNO Maker
- Raspberry Pi 3B+
- 5 DoF Robotic Arm
- A Full HD Web Camera
- Sugus Candies (Blackcurrant, Orange, and Strawberry)
- 1oz (30ml) Paper Sampling Cups
- 6 180-Degree Servo Motors

Currently, the robotic arm is programmed to perform 3 tasks:
- Picking up a small cup
- Picking up a sugus candy
- Sorting the sugus candies

<br clear="right"/>

***
### Usage:
<p align="center">
<img src="https://github.com/BradLoo51/A-Question-Answering-Approach-for-Cognitive-Understanding-of-A-5-Axis-Articulated-Robot-Control/assets/172585249/9d78b23a-a755-4161-aaea-71f0cf2cfdea"/>
The diagram above showcases the general setup to utilize the code
</p>

The ServoControl folder contains the code for the Arduino to receive serial communication from the Raspberry Pi and control the servo motors. The **main.py** in the Raspberry Pi folder should be executed first to allow it to connect with the Arduino and boot up the Yolov8 model. When the **main.py** finishes booting up, it will awaits for a connection from the computer's side before initializing the camera readings. The Chatbot-RASA folder contains all the necessary components to initialize the whole process.

Steps from the computer's side:
1. Open up two terminals in your source-code editor (VSCode)
2. Execute **rasa run actions** on one of the terminals (This will run a localhost server which will create a communication to the Raspberry Pi and handle all the actions that needs to be executed)
3. Execute **rasa run** on the other terminal (This will boot up the RASA Core model on a localhost server)
4. Finally, execute the **start.py** file to initialize the Speech Recognition modules where it will awaits specific keywords (Alexa or computer) before it starts detecting the voice commands

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Databases and services: Yolov8 model, RASA Core, RASA actions server,,###
Databases and services:,- Yolov8 model,- RASA Core model,- Speech Recognition modules,,###
- Yolov8 model,- RASA Core,- Speech Recognition,,###
Databases and services: Yolov8 model, RASA Core model, Speech Recognition modules,,###
- Yolov8 model,- RASA Core,- Speech Recognition modules,,###
None
- RASA,- Yolov8,,###
Databases and services:,- Yolov8 model,- RASA Core model,- Speech Recognition modules,,###
Databases and services: Yolov8 model, RASA Core, RASA actions server,,###
Databases and services:,- RASA,- Yolov8,- Speech Recognition,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Yolov8 model, RASA Core, RASA actions server, Speech Recognition modules

### Purpose of external services
- **Yolov8 model**: Used for object detection and computer vision tasks to identify and locate objects such as sugus candies and small cups.
- **RASA Core**: A framework for building conversational AI, used to understand and process user commands.
- **RASA actions server**: Handles the execution of actions based on the intents recognized by the RASA Core model.
- **Speech Recognition modules**: Used to convert spoken language into text, allowing the user to interact with the robotic arm through voice commands.