REQUEST
Problem: This is a README file from a Rasa chatbot repository <h1 align="center">Welcome to technocean-chat-bot 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="LICENCE" target="_blank">
    <img alt="License: ISC" src="https://img.shields.io/badge/License-ISC-yellow.svg" />
  </a>
  <a href="https://twitter.com/gdsclpu" target="_blank">
    <img alt="Twitter: gdsclpu" src="https://img.shields.io/twitter/follow/gdsclpu.svg?style=social" />
  </a>
</p>

> ChatBot Repo for TechNOcean Website

## Install Rasa Open Source

Ubuntu · macOS · Windows

- First make sure your pip version is up to date:
```sh
pip3 install -U pip
```

- Then install Rasa Open Source using pip:
```sh
pip3 install rasa
```

## Congratulations! You have successfully installed Rasa Open Source!

- You can now create a new project with:

```sh
rasa init
```

## Build for Production

- To build development version of the Rasa, run:

```sh
curl -sSL https://install.python-poetry.org | python3 -
git clone https://github.com/RasaHQ/rasa.git
cd rasa
poetry install
```

## Additional dependencies

- For some ML components, you will need to install additional dependencies. Which are not installed by default.
- To install them, run:

```sh
pip3 install rasa[full]
```

## Dependencies for spaCy

- spaCy is the recommended library for doing most NLU-related tasks in Rasa. To install it, run:

```sh
pip3 install rasa[spacy]
python3 -m spacy download en_core_web_md
```

## Run Project

- To train the project

```sh
rasa train
```

- To start the project in terminal

```sh
rasa shell
```

- To start the project

```sh
rasa run
```

- To start the project and avoid cors policy error

```sh
rasa run --cors "*"
```

- To run the actions, run this command in another terminal

```sh
rasa run actions
```

## Author

👤 **GDSC LPU**

* Website: https://gdsclpu.live/
* Twitter: [@gdsclpu](https://twitter.com/gdsclpu)
* Github: [@gdsclpu](https://github.com/gdsclpu)
* LinkedIn: [@gdsclpu](https://www.linkedin.com/company/gdsclpu/)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/gdsclpu/technocean-chat-bot/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2023 [GDSC LPU](https://github.com/gdsclpu).<br />
This project is [ISC](LICENCE) licensed.

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