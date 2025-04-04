import csv
import os

csv.field_size_limit(100000000)
INPUT_FOLDER_MD = 'results/10_results/'
INPUT_FOLDER_SD = 'results/09_results/'
RESULTS_FOLDER = 'results/11_results/'
FILES = [INPUT_FOLDER_SD + 'chatbot_repositories_sfsd_info.csv', INPUT_FOLDER_SD + 'chatbot_repositories_mfsd_info.csv', INPUT_FOLDER_MD + 'chatbot_repositories_sfmd_info.csv', INPUT_FOLDER_MD +'chatbot_repositories_mfmd_info.csv']
TYPES = ['sfsd', 'mfsd', 'sfmd', 'mfmd']
CSV_SEPARATOR = ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
MD_STATISTICS_FILE = RESULTS_FOLDER + 'md_statistics.txt'



def main(): 

    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)
    
    result_file = open(RESULTS_FOLDER + 'chatbots.csv', 'w', newline='', encoding="utf-8")
    

    for file, type in zip(FILES, TYPES):
        
        chatbot_file = open(file, 'r', encoding="utf-8")
        reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
        chatbots = list(reader)

        if type == 'sfsd':
            result_writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=reader.fieldnames + ['type'], extrasaction='ignore')
            result_writer.writeheader()
        
        for chatbot in chatbots:
            if type == 'mfmd' or type == 'sfmd':
                if chatbot['status'] == 'discarded':
                    continue
            chatbot['type'] = type
            result_writer.writerow(chatbot)


main()