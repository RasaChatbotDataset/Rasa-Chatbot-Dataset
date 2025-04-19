import ast
import os
import csv


RESULTS_FOLDER = 'results/16_results/'
INPUT_FOLDER = 'results/15_results/'
CHATBOT_FILE = 'chatbots.csv'
CSV_SEPARATOR= ';'

csv.field_size_limit(100000000)



def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open files
    chatbot_file = open(INPUT_FOLDER + CHATBOT_FILE, 'r', encoding='utf-8')
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    header = reader.fieldnames
    header.remove('wide-has-english')
    header.remove('has-english')

    result_file = open(RESULTS_FOLDER + CHATBOT_FILE, 'w', newline='', encoding='utf-8')
    writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=header)
    writer.writeheader()

    for chatbot in chatbots:
        chatbot['has-english'] = ast.literal_eval(chatbot['has-english'])
        recent = chatbot['version'] == '3.1' or chatbot['version'] == '3.6' or chatbot['version'] == '3.0'

        if chatbot['has-english'] and int(chatbot['stars']) > 0 and int(chatbot['n-actions-files']) > 0 and int(chatbot['n-entities']) > 0 and int(chatbot['n-slots']) > 0 and recent:
            del chatbot['wide-has-english']
            del chatbot['has-english']
            writer.writerow(chatbot)
    
    
    chatbot_file.close()
    result_file.close()





main()