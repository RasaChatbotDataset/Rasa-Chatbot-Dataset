REQUEST
Problem: This is a README file from a Rasa chatbot repository <!-- markdownlint-disable MD041-->
<p align="center">
    <a href="#readme">
        <img alt="WeatherWiz logo" src="https://raw.githubusercontent.com/pykong/weatherwiz/main/docs/header.png">
        <!-- Logo credits: Benjamin Felder -->
    </a>
</p>
<p align="center">
    <a href="#readme"><img alt="PlaceholderBadge" src="https://badgen.net/static/PyVersion/3.10/purple"></a>
    <a href="#readme"><img alt="PlaceholderBadge" src="https://badgen.net/static/Code-Quality/A+/green"></a>
    <a href="#readme"><img alt="PlaceholderBadge" src="https://badgen.net/static/Ruff/OK/green"></a>
    <a href="#readme"><img alt="PlaceholderBadge" src="https://badgen.net/static/Coverage/0.0/gray"></a>
    <a href="#readme"><img alt="PlaceholderBadge" src="https://badgen.net/static/MyPy/78.0/blue"></a>
    <a href="#readme"><img alt="PlaceholderBadge" src="https://badgen.net/static/Docs/0.0/gray"></a>
    <a href="https://github.com/pykong/weatherwiz/main/LICENSE">
        <img alt="License" src="https://badgen.net/static/license/MIT/blue">
    </a>
    <a href="#readme"><img alt="PlaceholderBadge" src="https://badgen.net/static/Build/1.0.0/pink"></a>
    <a href="#readme"><img alt="PlaceholderBadge" src="https://badgen.net/static/stars/★★★★★/yellow"></a>
</p>
<p align="center">
    <a href="#readme">
        <img alt="Example Dialog" src="https://github.com/pykong/weatherwiz/blob/main/docs/frontend.gif?raw=true">
    </a>
</p>

# WeatherWiz

WeatherWiz is a chatbot for weather forecasts.
It is built with [Rasa](https://rasa.com/), Python and love ❤️ and proudly **features**:

- a fancy frontend build with [chatroom.js](https://github.com/scalableminds/chatroom)
- using free APIs (_no signup or API key required_):
  - **real weather data** from [Bright Sky](https://brightsky.dev/docs/#/) API
    - forecasts up to seven days
    - historical data from 01.01.2010
  - geocoding via [Nominatim](https://nominatim.org/) API
  - user IP address as a location fallback via [ipinfo.io](https://ipinfo.io/) API
- slots for place and time for keeping conversation context
- a [dateparser](https://dateparser.readthedocs.io/en/latest/) for date and time extraction
- high test coverage via Pytest and Rasa's tests
- full Dockerization

## Getting started

To start WeatherWiz you will need:

- a working [Docker engine](https://docs.docker.com/engine/install/)
- Internet access (for setup and API access)
- at least 16GB RAM (32GB recommended)

Talking to WeatherWiz is as easy as:

1. Clone the project
2. Open a shell in the project folder
3. In the shell, run `docker compose up`
4. Open [localhost:8000](http://localhost:8000) in your browser
5. Enjoy talking to WeatherWiz... 🙂

## Contributing

WeatherWiz suggests the following development setup:

1. **Docker** to run the application
2. **Poetry** for dependency management
3. **Ruff** for formatting and linting
4. A type checker, preferably [pyright](https://github.com/microsoft/pyright)
5. **Pytest** for unit testing

Configuration is located in the `pyproject.toml`, at the root of the project.

To contribute:

1. Fork this repository
2. Do your changes, including:
   - test coverage
   - documentation
3. Open a PR

You may also feel free to open any issue.

## Current limitations

- WeatherWiz will only answer questions regarding rain, temperature and wind
- answer format remains generic
- failure of API access is not handled gracefully

## Links

- [dateparser](https://dateparser.readthedocs.io/en/latest/)
- [DateparserEntityExtractor](https://rasahq.github.io/rasa-nlu-examples/docs/extractors/dateparser/)
- [chatroom.js](https://github.com/scalableminds/chatroom)
- [Bright Sky](https://brightsky.dev/docs/#/)
- [Nominatim](https://nominatim.org/)
- [ipinfo.io](https://ipinfo.io/)

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
Bright Sky, Nominatim, ipinfo.io,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Bright Sky, Nominatim, ipinfo.io

## Purpose of external services

- **Bright Sky**: Provides real weather data including forecasts up to seven days and historical data from 01.01.2010.
- **Nominatim**: Used for geocoding to convert place names into geographic coordinates.
- **ipinfo.io**: Provides the user's IP address as a fallback for location information.