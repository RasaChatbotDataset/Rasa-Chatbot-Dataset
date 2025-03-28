import csv
import ast
import os
import zipfile

csv.field_size_limit(100000000)
INPUT_FOLDER = 'results/09_results/'
RESULTS_FOLDER = 'results/10_results/'
MD_FILES = ['chatbot_repositories_sfmd_info.csv', 'chatbot_repositories_mfmd_info.csv']
CSV_SEPARATOR = ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
MD_STATISTICS_FILE = RESULTS_FOLDER + 'md_statistics.txt'



def clean_same_domain(domain_files):

    zip_path = ZIP_FOLDER + '/' + domain_files[0]['full-name'].replace('/', '_') + '.zip'
    try:
        repository =  zipfile.ZipFile(zip_path, 'r')
    except:
        print(domain_files[0]['full-name'])
        return
    
    contents = {}
    n = 0
    
    for d in domain_files:

        full_domain_path = d['full-name'].split('/')[-1]+'-'+d['last-commit']+ '/' + d['domain-file']
        with repository.open(full_domain_path) as d_file:
            try:
                content = d_file.read().decode()
                contents[d['domain-file']] = content.replace(' ', '').replace('\n', '')
            except:
                print('Decode error')
                continue

    different_domain_files = []

    for d, c in contents.items():
        # First domain file
        if not different_domain_files:
            different_domain_files.append(d)
        else:
            for diff_domain in different_domain_files:
                # Domain file different from others already saved: save in list
                if c != contents[diff_domain]:
                   different_domain_files.append(d) 

    for d_file in domain_files[:]:
        if not d_file['domain-file'] in different_domain_files:
            domain_files.remove(d_file)
            n += 1
    return domain_files, n



def check_intersection(domain_files):

    fields = ['intents', 'entities', 'actions', 'slots', 'forms']
    for field in fields:
        complete_list = []
        for domain in domain_files:
            complete_list = complete_list + domain[field]
        
        if len(set(complete_list)) != len(complete_list):
            return True
    

    return False



def unify_domains(domain_files):

    union_domain = domain_files[0]

    for field in list(union_domain.keys())[11:]:

        for d in domain_files[1:]:
            if field == 'version':
                if union_domain[field] == 'unknown' and d[field] != 'unknown':
                    union_domain[field] = d[field]
            elif field.startswith('n-'):
                union_domain[field] += d[field]
            else:
                union_domain[field] = union_domain[field] + d[field]

    union_domain['domain-file'] = domain_files

    return union_domain
        

def write_statistics( domains_deleted_by_same, domains_deleted_by_merged, chatbots_all_merge, chatbots_all_same, manual_check):
    statistics_file = open(MD_STATISTICS_FILE, 'w', newline='')
    statistics_file.write(f"Domain files removed as copies: {domains_deleted_by_same}\n")
    statistics_file.write(f"Domain files removed after union: {domains_deleted_by_merged}\n")
    statistics_file.write(f"Chatbots completely unified: {chatbots_all_merge}\n")
    statistics_file.write(f"Chatbots with only domain file copies: {chatbots_all_same}\n")
    statistics_file.write(f"Chatbots left for manual check: {manual_check}\n")
    statistics_file.close()


def main(): 

    domains_deleted_by_same = 0
    domains_deleted_by_merged= 0
    chatbots_all_merge = 0
    chatbots_all_same = 0
    manual_check = 0

    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    for file in MD_FILES:
        
        chatbot_file = open(INPUT_FOLDER + file, 'r', encoding="utf-8")
        reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
        domains = list(reader)

        result_file = open(RESULTS_FOLDER + file, 'w', newline='', encoding="utf-8")
        result_writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=reader.fieldnames + ['status'], extrasaction='ignore')
        result_writer.writeheader()


        current_repo_id = None
        chatbot_domain_files = []

        for domain in domains:

            # Convert correct data type
            for field in list(domain.keys())[11:]:
                if field != 'version':
                    domain[field] = ast.literal_eval(domain[field])

            if domain['id'] != current_repo_id:

                # The previous repository is completed, ready to be checked
                if current_repo_id is not None:

                    # Check for same domain files
                    chatbot_domain_files, n = clean_same_domain(chatbot_domain_files)
                    domains_deleted_by_same += n
                   
                    if len(chatbot_domain_files) != 1:

                        # Check instersection
                        # Intersection between domain files but they are not the same file: manual check required
                        if check_intersection(chatbot_domain_files):
                            for d in chatbot_domain_files:
                                d['status'] = 'manual_check'
                                result_writer.writerow(d)
                                manual_check += 1
                        
                        # No intersection between domain files: domain split into more files
                        else:
                            union_domain = unify_domains(chatbot_domain_files)
                            domains_deleted_by_merged = domains_deleted_by_merged + len(chatbot_domain_files) - 1
                            union_domain['status'] = 'solved-union'
                            result_writer.writerow(union_domain)
                            chatbots_all_merge += 1

                    # Only one domain file left
                    else:
                        chatbot_domain_files[0]['status'] = 'solved-copies'
                        result_writer.writerow(chatbot_domain_files[0])
                        chatbots_all_same += 1
                    
                    # Previous repository analysis completed, start with new repository
                    current_repo_id = domain['id']
                    chatbot_domain_files = [domain]

                # No previous repository
                else:
                    chatbot_domain_files.append(domain)
                    current_repo_id = domain['id']
            else:
                chatbot_domain_files.append(domain)

        chatbot_file.close()
        result_file.close()

    write_statistics(domains_deleted_by_same, domains_deleted_by_merged, chatbots_all_merge, chatbots_all_same, manual_check)
                            



main()      
