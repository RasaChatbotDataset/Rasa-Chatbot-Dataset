import csv
import os
import ast

csv.field_size_limit(100000000)
INPUT_FOLDER_MD = os.path.join('results', '08_results')
INPUT_FOLDER_SD = os.path.join('results', '07_results')
RESULTS_FOLDER = os.path.join('results', '09_results')
FILES = [os.path.join(INPUT_FOLDER_SD, 'chatbot_repositories_sfsd_info.csv'), os.path.join(INPUT_FOLDER_SD, 'chatbot_repositories_mfsd_info.csv'), os.path.join(INPUT_FOLDER_MD, 'chatbot_repositories_sfmd_info.csv'), os.path.join(INPUT_FOLDER_MD, 'chatbot_repositories_mfmd_info.csv')]
TYPES = ['sfsd', 'mfsd', 'sfmd', 'mfmd']
CSV_SEPARATOR = ';'



def main():

    print('\n\n', '-'*20, 'CHATBOT FILES UNIFICATION', '-'*20, '\n') 

    # Result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)
    
    result_file = open(os.path.join(RESULTS_FOLDER, 'chatbots.csv'), 'w', newline='', encoding="utf-8")
    
    # For each chatbot file and type
    for file, type in zip(FILES, TYPES):
        
        chatbot_file = open(file, 'r', encoding="utf-8")
        reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
        chatbots = list(reader)

        print(f"{type.upper()} CHATBOTS: {len(chatbots)}")

        # Open result file
        if type == 'sfsd':
            header = reader.fieldnames + ['type']
            header[header.index('domain-file')] = 'domain-files'
            result_writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=header, extrasaction='ignore')
            result_writer.writeheader()
        
        for chatbot in chatbots:

            # Change domain name field for sd chatbots
            if type == 'sfsd' or type == 'mfsd':

                # Change single domain file to list of files
                chatbot['domain-files'] = [chatbot['domain-file']]
                del chatbot['domain-file']

            else:
                # Ignore dicarded chatbots
                if chatbot['status'] == 'discarded':
                    continue

                # Change single domain file to list of files
                if '[' not in chatbot['domain-file']:
                    chatbot['domain-files'] = [chatbot['domain-file']]
                    del chatbot['domain-file']

                # Change only field name
                else:
                    chatbot['domain-files'] = ast.literal_eval(chatbot['domain-file'])
                    del chatbot['domain-file']

            chatbot['type'] = type
            result_writer.writerow(chatbot)
    print('Step 9 completed')


main()