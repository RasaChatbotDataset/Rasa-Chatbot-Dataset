REQUEST
Problem: This is a README file from a Rasa chatbot repository ## Node.js backend with react static frontend working as a Single-page-app

To run this application locally you will need to have [Node.js](https://nodejs.org/en/) libary installed on your computer.

### Install
Run script `npm install` to install needed Node.js packages.

### Build
Run script `npm run build` to create a production build of the frontend.

### Starting the application
After Installing and Building the application can now be run locally with the command `npm start`.

In rasa folder:

Run Rasa server with `rasa run --enable-api --cors "*" --debug`.
Run Rasa Action server with `rasa run actions`

Visit [http://localhost:3001](http://localhost:3001) to view app in the browser.

### Clean
Run script `npm run clean` to remove the generated production build version of the frontend from the folder.

### MongoDB
Good instructions for installing and running mongo can be found [here](https://docs.mongodb.com/manual/administration/install-community/)

After setting up the database, run Rasa with the following command: `rasa run --enable-api --endpoints endpoints.yml --cors "*"`

Convert the conversation into a CSV log by running mongoService.js, e.g. `node services/eventLogger/logWriter.js`. The file is created in the logs directory, located in the project root.

To get a pretty Excel file, follow the instructions provided [here](https://support.affinity.co/hc/en-us/articles/360044453711-How-to-open-CSV-files-with-the-correct-delimiter-separator)

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    MongoDB,,###
MongoDB,,###
MongoDB,,###
MongoDB,,###
MongoDB,,###
MongoDB,,###
MongoDB,,###
MongoDB,,###
MongoDB,,###
MongoDB,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
MongoDB

### Purpose of external services
MongoDB: MongoDB is used to store and manage the conversation logs generated by the chatbot. This allows for the storage, retrieval, and analysis of conversation data.