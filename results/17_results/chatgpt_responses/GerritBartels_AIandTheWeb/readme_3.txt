REQUEST
Problem: This is a README file from a Rasa chatbot repository # Flask Search Engine

This project is a simple search engine built with Flask, Whoosh or a custom index, and a custom web crawler.

## Showcase

![SearchEngineShowcase](https://github.com/GerritBartels/AIandTheWeb/assets/64156238/952c1e69-4d9a-4234-993f-16e557dafd26)

## Features

- **Web Crawling**: The search engine uses a custom-built web crawler to fetch and index web pages. The crawler can be run in parallel using multiple threads for increased performance.
- **Search**: The search engine uses Whoosh, a fast, featureful full-text indexing and searching library or our custom implementation, to index and search the crawled web pages.
- **Web Interface**: The search engine provides a simple yet visually appealing web interface built with Flask. Users can enter their search queries and get the search results displayed in a user-friendly format.

## Usage

1. Clone the repository.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask app: `python flask_search_engine.py`

## Configuration

You can configure the search engine by modifying the following variables in `flask_search_engine.py`:

- `START_URL`: The URL where the web crawler starts crawling.
- `INDEX_DIR_NAME`: The directory where the index is stored.
- `LOAD_INDEX_FROM_FILE`: Whether to load the index from file. If set to `False`, the web crawler will start crawling and build the index.
- `NUM_THREADS`: The number of threads used by the web crawler.
- `DEBUG`: Whether to run the Flask app in debug mode.

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