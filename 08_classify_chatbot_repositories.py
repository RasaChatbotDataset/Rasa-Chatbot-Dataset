import csv
import ast
import copy
import os

CSV_SEPARATOR= ';'
RESULTS_FOLDER = 'results/08_results'
CHATBOTS_FILE_NAME = 'results/07_results/chatbot_repositories_files.csv'
MFSD_CHATBOTS_FILE_NAME = RESULTS_FOLDER + '/' + 'chatbot_repositories_mfsd.csv'
SFSD_CHATBOTS_FILE_NAME = RESULTS_FOLDER + '/' + 'chatbot_repositories_sfsd.csv'
MFMD_CHATBOTS_FILE_NAME = RESULTS_FOLDER + '/' + 'chatbot_repositories_mfmd.csv'
SFMD_CHATBOTS_FILE_NAME = RESULTS_FOLDER + '/' + 'chatbot_repositories_sfmd.csv'

fields = ['id', 'full-name', 'html-url', 'stars', 'forks', 'created-at', 'updated-at', 'pushed-at', 'default-branch', 'owner-name', 'owner-id','owner-type',
          'last-commit', 'last-commit-date', 'domain-folder', 'domain-files', 'n-domain-files', 'nlu-files' , 'n-nlu-files', 'actions-files', 
          'n-actions-files', 'readme-files', 'n-readme-files', 'language-files', 'n-language-files','unclear-match']

# Split a multi-domain repository into more chatbots
def split_sub_folders(chatbot, mfsd_writer, mfmd_writer):

    chatbot['domain-folders']  = ast.literal_eval(chatbot['domain-folders'])
    chatbot['domain-files']  = ast.literal_eval(chatbot['domain-files'])
    chatbot['nlu-files'] = ast.literal_eval(chatbot['nlu-files'])
    chatbot['actions-files'] = ast.literal_eval(chatbot['actions-files'])
    chatbot['language-files'] = ast.literal_eval(chatbot['language-files'])
    chatbot['readme-files'] = ast.literal_eval(chatbot['readme-files'])

    # Compute NLU files match score with domain folders
    nlu_scores = []

    for nlu in chatbot['nlu-files']:
        scores = []
        
        for domain in chatbot['domain-folders']:
            score = compute_score_match(domain, nlu)
            scores.append(score)
        nlu_scores.append(scores)
    
    # Compute actions files match score with domain folders
    actions_scores = []

    for action in chatbot['actions-files']:
        scores = []

        for domain in chatbot['domain-folders']:
            score = compute_score_match(domain, action)
            scores.append(score)
        actions_scores.append(scores)
    
    # Compute readme files match score with domain folders
    readme_scores = []

    for readme in chatbot['readme-files']:
        scores = []

        for domain in chatbot['domain-folders']:
            if readme == 'README.md':
                score = -1  # Each sub-chatbot will keep the main readme
            else:
                score = compute_score_match(domain, readme)
            scores.append(score)
        readme_scores.append(scores)
    
    # Compute language files match score with domain folders
    language_scores = []

    for language in chatbot['language-files']:
        scores = []

        for domain in chatbot['domain-folders']:
            score = compute_score_match(domain, language)
            scores.append(score)
        language_scores.append(scores)
    
    # Create a sub-chatbot for each domain folder
    i = 0
    for domain_folder in chatbot['domain-folders']:

        sub_chatbot =  copy.deepcopy(chatbot)
        sub_chatbot['unclear-match'] = []

        sub_chatbot['domain-folder'] = domain_folder

        if domain_folder != '.':
            domain_folder = './' +domain_folder

        # Select domain files for sub-chatbot
        sub_chatbot['domain-files'] = []
        for domain in chatbot['domain-files']:
            domain = './' + domain

            if domain_folder == domain[0:domain.rfind('/')]:
                sub_chatbot['domain-files'].append(domain[2:])
        
        sub_chatbot['n-domain-files'] = len(sub_chatbot['domain-files'])

        # Select NLU files for sub-chatbot
        sub_chatbot['nlu-files'] = []

        for j in range(len(nlu_scores)):
            scores = nlu_scores[j]
            if scores.index(max(scores)) == i:
                if scores.count((max(scores))) == 1:
                    sub_chatbot['nlu-files'].append(chatbot['nlu-files'][j])
                else: 
                    sub_chatbot['unclear-match'].append(chatbot['nlu-files'][j])

        sub_chatbot['n-nlu-files'] = len(sub_chatbot['nlu-files'])

        # Select actions files for sub-chatbots
        sub_chatbot['actions-files'] = []
        
        for k in range(len(actions_scores)):
            scores = actions_scores[k]
            if scores.index(max(scores)) == i:
                if scores.count((max(scores))) == 1:
                    sub_chatbot['actions-files'].append(chatbot['actions-files'][k])
                else:
                    sub_chatbot['unclear-match'].append(chatbot['actions-files'][k])
        
        sub_chatbot['n-actions-files'] = len(sub_chatbot['actions-files'])

        # Select language files for sub-chatbots
        sub_chatbot['language-files'] = []
        
        for l in range(len(language_scores)):
            scores = language_scores[l]
            if scores.index(max(scores)) == i:
                if scores.count((max(scores))) == 1:
                    sub_chatbot['language-files'].append(chatbot['language-files'][l])
                else:
                    sub_chatbot['unclear-match'].append(chatbot['language-files'][l])
        
        sub_chatbot['n-language-files'] = len(sub_chatbot['language-files'])

        # Select readme files for sub-chatbots
        sub_chatbot['readme-files'] = []
        
        for h in range(len(readme_scores)):
            scores = readme_scores[h]
            if max(scores) == -1:
                sub_chatbot['readme-files'].append(chatbot['readme-files'][h])
            elif scores.index(max(scores)) == i:
                if scores.count((max(scores))) == 1:
                    sub_chatbot['readme-files'].append(chatbot['readme-files'][h])
                else:
                    sub_chatbot['unclear-match'].append(chatbot['readme-files'][h])
        
        sub_chatbot['n-readme-files'] = len(sub_chatbot['readme-files'])

        # Sub-chatbot id
        sub_chatbot['id'] = sub_chatbot['full-name'] + '__' + sub_chatbot['domain-folder']
        
        if sub_chatbot['n-domain-files'] == 1:
            mfsd_writer.writerow(sub_chatbot)
        else:
            mfmd_writer.writerow(sub_chatbot)
        i +=1


# Compute match score between domain folder and file
def compute_score_match(domain_folder, file):
    file = './' + file
    if domain_folder != '.':
        domain_folder = './' +domain_folder

    # Split file and domain path in folder tokens
    domain_tokens = domain_folder.split('/')
    file_folder_tokens = file[0:file.rfind('/')].split('/')
    min_tokens = min(len(domain_tokens), len(file_folder_tokens))

    score = 0
    # One point for each subsequential token in common
    for t in range(min_tokens):
        if domain_tokens[t] == file_folder_tokens[t]:
            score +=1
    
    # Normalize by dividing by total number of tokens
    score = score / (len(domain_tokens) + len(file_folder_tokens))
    return score



def main():

    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open files
    csv.field_size_limit(100000000)
    chatbot_file = open(CHATBOTS_FILE_NAME, 'r', encoding="utf-8")
    reader = csv.DictReader(chatbot_file, delimiter=CSV_SEPARATOR)
    chatbots = list(reader)

    sfsd_file = open(SFSD_CHATBOTS_FILE_NAME, 'w', newline='', encoding="utf-8")
    sfsd_writer = csv.DictWriter(sfsd_file, delimiter=CSV_SEPARATOR, fieldnames=fields[:-1], extrasaction='ignore')
    sfsd_writer.writeheader()

    sfmd_file = open(SFMD_CHATBOTS_FILE_NAME, 'w', newline='', encoding="utf-8")
    sfmd_writer = csv.DictWriter(sfmd_file, delimiter=CSV_SEPARATOR, fieldnames=fields[:-1], extrasaction='ignore')
    sfmd_writer.writeheader()

    mfmd_file = open(MFMD_CHATBOTS_FILE_NAME, 'w', newline='', encoding="utf-8")
    mfmd_writer = csv.DictWriter(mfmd_file, delimiter=CSV_SEPARATOR, fieldnames=fields, extrasaction='ignore')
    mfmd_writer.writeheader()

    mfsd_file = open(MFSD_CHATBOTS_FILE_NAME, 'w', newline='', encoding="utf-8")
    mfsd_writer = csv.DictWriter(mfsd_file, delimiter=CSV_SEPARATOR, fieldnames=fields, extrasaction='ignore')
    mfsd_writer.writeheader()


    # Split multi-domain folder repositories, keep single-domain folder ones
    for chatbot in chatbots:

        # Single folder (SF)
        if int(chatbot['n-domain-folders']) == 1: 

            del chatbot['n-domain-folders']
            chatbot['domain-folder'] = chatbot['domain-folders'][2:-2]
            del chatbot['domain-folders']

            # Chatbot id
            chatbot['id'] = chatbot['full-name']

            # Single folder multi domain (SFMD)
            if int(chatbot['n-domain-files']) > 1: 
                sfmd_writer.writerow(chatbot)

            # Single folder single domain (SFSD)
            else:
                sfsd_writer.writerow(chatbot)

        # Multi folder (MF)
        else:                                
            split_sub_folders(chatbot, mfsd_writer, mfmd_writer)


    # Close files
    mfmd_file.close()
    mfsd_file.close()
    sfmd_file.close()
    sfsd_file.close()
    chatbot_file.close()

main()
