import csv
import os
import ast

CSV_SEPARATOR = ';'
INPUT_FOLDER = 'results/18_results/'
RESULTS_FOLDER = 'results/19_results/'
CHATBOT_FILE = 'chatbots.csv'
STATISTICS = 'blacklist-statistics.txt'


def main():
    removed_services = 0
    no_more_services = 0

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open files
    csv.field_size_limit(100000000)
    chatbot_file = open(INPUT_FOLDER + CHATBOT_FILE, 'r', encoding="utf-8")
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    bl_file = open('19_services_black_list.csv', 'r', encoding="utf-8")
    blacklist = bl_file.read().split(CSV_SEPARATOR)
    print(blacklist)

    result_file = open(RESULTS_FOLDER + '1_' + CHATBOT_FILE, 'w', newline='', encoding="utf-8")
    writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=reader.fieldnames, extrasaction='ignore')
    writer.writeheader()

    for chatbot in chatbots:

        if chatbot['external-services-actions']:
            chatbot['external-services-actions'] = ast.literal_eval(chatbot['external-services-actions'])
        if chatbot['external-services-readme']:
            chatbot['external-services-readme'] = ast.literal_eval(chatbot['external-services-readme'])
            n_readme = int(chatbot['n-external-services-readme'])
        else:
            n_readme = 0
        had_services = (int(chatbot['n-external-services-actions']) + n_readme) > 0

        for b_service in blacklist:
            if chatbot['external-services-actions']:
                for s in chatbot['external-services-actions']:
                    if s.lower() == b_service:
                        chatbot['external-services-actions'].remove(s)
                        removed_services += 1
            if chatbot['external-services-readme']:
                for s in chatbot['external-services-readme']:
                    if s.lower() == b_service:
                        chatbot['external-services-readme'].remove(s)
                        removed_services += 1
        
        if chatbot['external-services-actions']:
            chatbot['n-external-services-actions'] = len(chatbot['external-services-actions'])
        if chatbot['external-services-readme']:
            chatbot['n-external-services-readme'] = len(chatbot['external-services-readme'])
        if had_services and chatbot['n-external-services-actions'] == 0 and chatbot['n-external-services-readme'] == 0:
            no_more_services += 1

        writer.writerow(chatbot)
    
    statistics_file = open(RESULTS_FOLDER + STATISTICS, 'w', newline='')
    statistics_file.write('SERVICES REMOVED: '+ str(removed_services))
    statistics_file.write('\nCHATBOTS WITH NO MORE SERVICES: '+ str(no_more_services))

    
    chatbot_file.close()
    bl_file.close()
    result_file.close()
    statistics_file.close()

main()