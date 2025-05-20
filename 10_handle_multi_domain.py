import csv
import ast
import os
import zipfile
import yaml
from deepdiff import DeepDiff

csv.field_size_limit(100000000)
INPUT_FOLDER = 'results/09_results/'
RESULTS_FOLDER = 'results/10_results/'
MD_FILES = ['chatbot_repositories_sfmd_info.csv', 'chatbot_repositories_mfmd_info.csv']
CSV_SEPARATOR = ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
MD_STATISTICS_FILE = RESULTS_FOLDER + 'md_statistics.txt'


# Remove domain copies
def clean_same_domain(domain_files):

    # Open zip file
    zip_path = ZIP_FOLDER + '/' + domain_files[0]['full-name'].replace('/', '_') + '.zip'
    try:
        repository =  zipfile.ZipFile(zip_path, 'r')
    except:
        print(domain_files[0]['full-name'])
        return
    
    # Store different domain contents
    contents = {}
    n = 0
    
    # For each domain file
    for d in domain_files:

        full_domain_path = d['full-name'].split('/')[-1]+'-'+d['last-commit']+ '/' + d['domain-file']
        with repository.open(full_domain_path) as d_file:
            try:
                # Retrieve content
                file_content = d_file.read().decode()
                yml_content = yaml.safe_load(file_content)
                contents[d['domain-file']] = yml_content
            except:
                print('Decode error')
                continue

    # Store different domain file names
    different_domain_files = []

    for d, c in contents.items():
        # First domain file
        if not different_domain_files:
            different_domain_files.append(d)
        # Not first domain file
        else:
            is_new = True
            # If content already present in contents: not a new domain
            for diff_domain in different_domain_files:

                # Copy found: domain not new
                if not DeepDiff(c, contents[diff_domain], ignore_order=True):
                    is_new = False
                    break
                   
            # YML domain different from others already saved: save in list  
            if is_new: 
                different_domain_files.append(d) 

    # Remove domain copies
    for d_file in domain_files[:]:
        if not d_file['domain-file'] in different_domain_files:
            domain_files.remove(d_file)
            n += 1

    return domain_files, n


# Check if chatbot domain files have intersection
def check_intersection(domain_files):

    fields = ['intents', 'entities', 'actions', 'slots', 'forms']
    for field in fields:
        complete_list = []
        for domain in domain_files:
            complete_list = complete_list + domain[field]
        
        # Set shorter than union list: domain files have intersection 
        if len(set(complete_list)) != len(complete_list):
            return True
    
    return False


# Unify domain parameters
def unify_domains(domain_files):

    union_domain = domain_files[0]
    domain_files_names = [domain_files[0]['domain-file']]

    for d in domain_files[1:]:

        domain_files_names.append(d['domain-file'])

        for field in list(union_domain.keys())[11:]:
            # Keep the known version if defined
            if field == 'version':
                if union_domain[field] == 'unknown' and d[field] != 'unknown':
                    union_domain[field] = d[field]
            # Sum numeric parameters
            elif field.startswith('n-'):
                union_domain[field] += d[field]
            # Unify lists
            else:
                union_domain[field] = union_domain[field] + d[field]

    union_domain['domain-file'] = domain_files_names

    return union_domain

# Check domain files of a chatbot
def check_repository(chatbot_domain_files, result_writer, statistics):
    # Check for same domain files
    chatbot_domain_files, n = clean_same_domain(chatbot_domain_files)
    statistics['domains_deleted_by_same'] += n
    
    if len(chatbot_domain_files) != 1:

        # Check instersection
        # Intersection between domain files but they are not the same file: discard
        if check_intersection(chatbot_domain_files):
            for d in chatbot_domain_files:
                d['status'] = 'discarded'
                result_writer.writerow(d)
            statistics['discarded'] += 1
        
        # No intersection between domain files: domain split into more files
        else:
            union_domain = unify_domains(chatbot_domain_files)
            statistics['domain_merged'] = statistics['domain_merged'] + len(chatbot_domain_files)
            union_domain['status'] = 'solved-union'
            result_writer.writerow(union_domain)
            statistics['chatbots_all_merge'] += 1

    # Only one domain file left
    else:
        chatbot_domain_files[0]['status'] = 'solved-copies'
        result_writer.writerow(chatbot_domain_files[0])
        statistics['chatbots_all_same'] += 1
    
        
# Save cleaning statistics
def write_statistics(statistics):
    statistics_file = open(MD_STATISTICS_FILE, 'w', newline='')
    statistics_file.write(f"Domain file copies removed: {statistics['domains_deleted_by_same']}\n")
    statistics_file.write(f"Domain files merged: {statistics['domain_merged']}\n")
    statistics_file.write(f"Chatbots solved by domain files merge: {statistics['chatbots_all_merge']}\n")
    statistics_file.write(f"Chatbots solved by domain copies removal: {statistics['chatbots_all_same']}\n")
    statistics_file.write(f"Chatbots discarded: {statistics['discarded']}\n")
    statistics_file.close()


def main(): 

    # Statistics fields
    statistics = {
        'domains_deleted_by_same': 0,
        'domain_merged': 0,
        'chatbots_all_merge': 0,
        'chatbots_all_same': 0,
        'discarded': 0
    }

    # Result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    for file in MD_FILES:
        
        # Open files
        chatbot_file = open(INPUT_FOLDER + file, 'r', encoding="utf-8")
        reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
        domains = list(reader)

        result_file = open(RESULTS_FOLDER + file, 'w', newline='', encoding="utf-8")
        result_writer = csv.DictWriter(result_file, delimiter=CSV_SEPARATOR, fieldnames=reader.fieldnames + ['status'], extrasaction='ignore')
        result_writer.writeheader()

        # Current chatbot id
        current_repo_id = None
        # Domain list of current chatbot
        chatbot_domain_files = []

        for domain in domains:

            # Convert correct data type
            for field in list(domain.keys())[11:]:
                if field != 'version':
                    domain[field] = ast.literal_eval(domain[field])

            # Check new domain file's chatbot id
            if domain['id'] != current_repo_id:

                # The previous chatbot is completed, ready to be checked
                if current_repo_id is not None:
                    
                    check_repository(chatbot_domain_files, result_writer, statistics)
                    # Previous chatbot analysis completed, start with new chatbot
                    current_repo_id = domain['id']
                    chatbot_domain_files = [domain]

                # No previous chatbot
                else:
                    chatbot_domain_files.append(domain)
                    current_repo_id = domain['id']
            # Same id as current chatbot: append domain file to list
            else:
                chatbot_domain_files.append(domain)
        
        # Handle last repository
        check_repository(chatbot_domain_files, result_writer, statistics)

        # Close files
        chatbot_file.close()
        result_file.close()

    write_statistics(statistics)
                            

main()      
