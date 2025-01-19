from utils import download_clean_zip
import csv
import os
from utils import sync



CSV_SEPARATOR = ';'
CHATBOTS_FILE = 'not-downloaded-chatbots-2025.csv'
ZIP_DIRECTORY = 'chatbot_zip-2025'

def main():

    if not os.path.isdir(ZIP_DIRECTORY):
        os.makedirs(ZIP_DIRECTORY)

    chatbot_file = open(CHATBOTS_FILE, 'r', newline='')
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)
    i=0
    for chatbot in chatbots[2:10]:
        i += 1
        if i%50==0:
         sync(ZIP_DIRECTORY)

        download_clean_zip(ZIP_DIRECTORY, chatbot['full-name'], chatbot['last-commit'])
        print(f"{chatbot['full-name']}: downloaded and cleaned")
    
    sync(ZIP_DIRECTORY)
    chatbot_file.close()

main()
