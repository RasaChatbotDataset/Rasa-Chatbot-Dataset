import ast
import os
import csv


RESULTS_FOLDER = os.path.join('results', '15_results')
INPUT_FOLDER = os.path.join('results', '14_results')
CHATBOT_FILE = 'chatbots.csv'
CSV_SEPARATOR= ';'

csv.field_size_limit(100000000)



def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    print('\n\n', '-'*20, 'CHATBOT SELECTION', '-'*20, '\n') 

    # Open files
    chatbot_file = open(os.path.join(INPUT_FOLDER, CHATBOT_FILE), 'r', encoding='utf-8')
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    header = reader.fieldnames
    header.remove('has-english')

    result_file = open(os.path.join(RESULTS_FOLDER, CHATBOT_FILE), 'w', newline='', encoding='utf-8')
    writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=header)
    writer.writeheader()

    selected_chatbots = 0

    # Select chatbots
    for chatbot in chatbots:
        chatbot['has-english'] = ast.literal_eval(chatbot['has-english'])
        recent = chatbot['version'] == '3.1' or chatbot['version'] == '3.6' or chatbot['version'] == '3.0'

        if chatbot['has-english'] and int(chatbot['stars']) > 0 and int(chatbot['n-actions-custom']) > 0 and (int(chatbot['n-entities']) > 0 or int(chatbot['n-slots']) > 0) and recent:
            del chatbot['has-english']
            writer.writerow(chatbot)
            selected_chatbots += 1
    
    # Close files
    chatbot_file.close()
    result_file.close()
    print('Step 15 completed')
    print(f"Chatbots selected: {selected_chatbots}")





main()