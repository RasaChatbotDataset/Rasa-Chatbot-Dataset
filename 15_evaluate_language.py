import detectlanguage
import yaml
import zipfile
import ast
import os
import re
import csv

RESULTS_FOLDER = 'results/15_results/'
INPUT_FILE = RESULTS_FOLDER + 'chatbots_language_check.csv'
OUTPUT_FILE = RESULTS_FOLDER + 'chatbots2.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'


def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open files
    csv.field_size_limit(100000000)
    chatbot_file = open(INPUT_FILE, 'r', encoding="utf-8")
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    result_file = open(OUTPUT_FILE, 'w', newline='', encoding="utf-8")
    header = reader.fieldnames + ['languages', 'has-english', 'pure-english']
    writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=header)
    writer.writeheader()
    

    for chatbot in chatbots:

        #print(chatbot['id'])
        # Sort languages list
        if chatbot['training-language']:
            chatbot['training-language'] = ast.literal_eval(chatbot['training-language'])
            chatbot['training-language'].sort()
        else:
            chatbot['training-language'] = []
        if chatbot['config-languages']:
            chatbot['config-languages'] = ast.literal_eval(chatbot['config-languages'])
            chatbot['config-languages'].sort()
        else:
            chatbot['config-languages'] = []
        if chatbot['response-languages']:
            chatbot['response-languages'] = ast.literal_eval(chatbot['response-languages'])
            chatbot['response-languages'].sort()
        else:
            chatbot['response-languages'] = []

        # Extract language
        chatbot['languages'] = list(set(chatbot['training-language'] + chatbot['response-languages']))
        chatbot['languages'].sort()

        chatbot['has-english'] = False
        chatbot['pure-english'] = False

        # English in training languages, response languages and in config languages if config languages not empty
        if 'en' in chatbot['training-language'] and 'en' in chatbot['response-languages'] and (not chatbot['config-languages'] or 'en' in chatbot['config-languages']):

            chatbot['has-english'] = True

            # English is the only language
            if len(chatbot['training-language'] ) <= 1 and len(chatbot['response-languages']) <= 1 and len(chatbot['config-languages']) <= 1:
                chatbot['pure-english'] = True
        

        # Write chatbot 
        if chatbot['languages']:       
            writer.writerow(chatbot)

    # Close files
    chatbot_file.close()
    result_file.close()



main()