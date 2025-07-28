REQUEST
Problem: This is a README file from a Rasa chatbot repository # Entity Extraction from Flipkart's page and building a Chatbot #
This project is focused on extracting relevant entities such as product name, price, ratings, etc from Flipkart for differnt products.The scraped data is used for making a chatbot that can provide users with information about the product, making it easier for users to get information about products they are interested in.
## Requirements
* Python
* Pycharm
* Pandas
* Numpy
* Requests
* Beautiful Soup
## Installation
* Python: https://www.python.org/downloads/
* PyCharm: https://www.jetbrains.com/pycharm/download/
* Rasa: pip install rasa
* Requests: pip install requests
* BeautifulSoup: pip install beautifulsoup4
* Pandas: pip install pandas
* Numpy: pip install numpy
## Project Workflow
1. Scrape required data from the webpage of Flipkart using Requests and BeautifulSoup.
2. Process the scraped data to extract relevant entities such as product name, price, ratings, etc.
3. Convert the extracted data into a structured format such as CSV file.
4. Use Rasa to build a chatbot that can respond to user queries related to Flipkart products and related queries.
5. Train the chatbot using the extracted product data to improve its accuracy and responsiveness.
## Output
The output of this project is a chatbot that can assist users in obtaining information about Flipkart products. By using the extracted entities such as product name, price, ratings, etc., the chatbot can provide users with accurate and relevant information about products they are interested in. This can help users make informed purchasing decisions and to improve their overall shopping experience.

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