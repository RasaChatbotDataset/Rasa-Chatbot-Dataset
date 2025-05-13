REQUEST
Problem: This is a README file from a Rasa chatbot repository # Flask Movie Recommender

This project is a movie recommender system developed using Flask, Flask-User, Flask-Sqlalchemy, TensorFlow, and the MovieLens 100k dataset. It seamlessly combines intuitive user interaction, robust database management, and neural network-based recommendations.

## Showcase

![Movie_Recommender_Demo](https://github.com/GerritBartels/AIandTheWeb/assets/64156238/3e6353cd-8d73-426d-ab9b-3bf0902835ef)


## Features

- **Web Interface**: The movie recommender provides a sleek, visually appealing web interface built with Flask. Users can register or log in to browse a list of stored films, give them their personal ratings, query the database for their favorite movies, or get custom recommendations on what to watch next from a neural recommendation model created with TensorFlow. Navigation is facilitated by a burger menu and a navigation bar.
- **User Management**:  Flask-User handles the registration, login, and logout processes. Certain routes are protected and accessible only to logged-in users, ensuring a secure and personalized experience.
- **Relational databases**: All data is stored in SQLite databases for efficient access, including adding new data and updating data.
- **Homepage**: The homepage welcomes all visitors with a carousel overview of top movies, a varying selection of films to discover, and links to the other features.
- **Movies**: Logged-in users can browse through a list of all stored films and view additional information such as the average star rating, the film poster, the plot description, and links to IMDb and TMDB. In addition, users have the option of rating each film using a star system or adjusting their previous rating.
- **Search**: Logged-in users can query the movie database, with the results being fuzzily matched based on the Levenshtein Distance to overcome spelling mistakes. Internally, flask-sqlalchemy is used to make queries in a simple, object-oriented way without using SQL directly.
- **Neural Recommender**: A neural recommendation model created with TensorFlow provides logged-in users with movie suggestions. Both movies and users are represented by learned embeddings that guide the neural network for providing personalized recommendations. The cold start problem is addressed by assigning new users the average embedding calculated across all users.
- **Scheduled Training**: The neural recommendation model is kept up-to-date by being regularly retrained as soon as a certain number of new user interactions have been recorded. This ensures the system continuously adapts to evolving user preferences.


## Usage

1. Clone the repository. 
2. Change directory: `cd MovieRecommender`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Instantiate the database: `flask --app recommender.py initdb`
   4.1 To entirely rebuild an existing database add the `--rebuild` flag
5. Train the recommender: `flask --app recommender.py train`
6. Run the Flask app: `python recommender.py`

Optionally the larger variants of the [MovieLens](https://grouplens.org/datasets/movielens/) dataset may be used if desired. 

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    SQLite, IMDb, TMDB, MovieLens,,##
SQLite, IMDb, TMDB, MovieLens,,##
- SQLite,- MovieLens dataset,- IMDb,- TMDB,,##
SQLite, IMDb, TMDB,,##
SQLite, IMDb, TMDB, MovieLens,,##
- SQLite,- MovieLens dataset,- IMDb,- TMDB,,##
SQLite, IMDb, TMDB, MovieLens,,##
SQLite, IMDb, TMDB, MovieLens,,##
SQLite, IMDb, TMDB, MovieLens,,##
SQLite, IMDb, TMDB, MovieLens,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
SQLite, IMDb, TMDB, MovieLens

## Purpose of external services

- **SQLite**: Used for efficient access, storage, and management of all data within the application.
- **IMDb**: Provides additional information about movies such as ratings, plot descriptions, and links.
- **TMDB**: Offers movie posters, plot descriptions, and other movie-related data.
- **MovieLens**: Supplies the dataset used for training the neural recommendation model.