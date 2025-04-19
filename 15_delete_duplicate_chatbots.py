import zipfile
import ast
import os
import pandas as pd
from difflib import SequenceMatcher


RESULTS_FOLDER = 'results/15_results/'
INPUT_FOLDER = 'results/14_results/'
CHATBOT_FILE = 'chatbots.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
DATE_FILES = ['results/08_results/chatbot_repositories_sfsd.csv', 'results/08_results/chatbot_repositories_mfsd.csv', 'results/08_results/chatbot_repositories_sfmd.csv', 'results/08_results/chatbot_repositories_mfmd.csv']

FIELDS = ['intents', 'entities', 'actions', 'slots','slots-type', 'forms', 'config-languages', 'training-language', 'response-languages', 'n-actions-files']

ORDER_COLUMNS = ['id', 'full-name', 'html-url', 'stars', 'forks', 'owner-name', 'owner-type', 'created-at', 'last-commit', 'last-commit-date', 'domain-files', 'type', 'n-intents', 'intents', 'n-entities', 'entities', 'n-actions', 'actions', 'n-slots', 'slots', 'n-slots-from-entity', 'n-slots-from-text', 'slots-type', 'n-forms', 'forms', 'version', 'config-languages', 'training-language', 'response-languages', 'wide-has-english', 'has-english', 'pure-english', 'n-actions-files']
           
def select_best_copies(copies):

    # The first copy is the best one based on our sorting
    best_copies = []
    diff_action_files = []

    # No action file: keep only best one
    if copies[0]['n-actions-files'] == 0:
        best_copies = [copies[0]]

    # One action file: check content
    elif copies[0]['n-actions-files'] == 1:
        for copy in copies:

            # Open zip
            zip_path = ZIP_FOLDER + '/' + copy['full-name'].replace('/', '_') + '.zip'
            try:
                repository =  zipfile.ZipFile(zip_path, 'r')
            except:
                print(copy['full-name'])
                return
        
            # Check action file
            action_file = ast.literal_eval(copy['actions-files'])[0]
            full_action_path = copy['full-name'].split('/')[-1]+'-'+copy['last-commit']+ '/' + action_file
            with repository.open(full_action_path) as d_file:
                try:
                    content = d_file.read().decode()
                    clean_content = content.strip().replace('\n', '').replace(' ', '')
                    # Verify file similarity with others already saved
                    is_new = True
                    for c in diff_action_files:
                        if SequenceMatcher(None, clean_content, c).ratio() >= 0.95:
                            is_new = False
                            break
                    if is_new:
                    #if clean_content not in diff_action_files: 
                        diff_action_files.append(clean_content)
                        best_copies.append(copy)

                except Exception as e:
                    print(f"Decode error for {copy['id']}")
                    print(e)
                    continue

    # Multiple action files: check names
    else:

        for copy in copies:

            # Get clean action file name
            action_files = ast.literal_eval(copy['actions-files'])
            clean_action_files = []
            for action_file in action_files:
                clean_action_files.append(action_file.split('/')[-1])
            
            # Sort
            clean_action_files.sort()

            if clean_action_files not in diff_action_files:
                diff_action_files.append(clean_action_files)
                best_copies.append(copy)


    return best_copies



def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Open files
    chatbots= pd.read_csv(INPUT_FOLDER + CHATBOT_FILE, sep=CSV_SEPARATOR)

    # Join with relevant fields
    cb_files = pd.DataFrame()
    for file in DATE_FILES:
        cb_with_files = pd.read_csv(file, sep=CSV_SEPARATOR)
        cb_with_files = cb_with_files[['id', 'created-at', 'owner-name', 'owner-type', 'last-commit-date', 'actions-files']]
        cb_files = pd.concat([cb_files, cb_with_files])
    chatbots = pd.merge(chatbots, cb_files, how='inner', on=['id'])
    chatbots.to_csv(RESULTS_FOLDER + 'chatbots_join_date.csv', sep=CSV_SEPARATOR, index=False)
    
    # Order chatbots to have copies one after another
    order_fields = FIELDS + ['version', 'stars', 'forks', 'created-at'] # TODO: rivedere insieme priorià 
    # <3.0 becomes 1.5
    chatbots['version'] = chatbots['version'].replace('<3.0', '1.5')
    chatbots[['n-entities', 'n-slots', 'n-slots-from-text', 'n-slots-from-entity', 'n-forms']] = chatbots[['n-entities', 'n-slots', 'n-slots-from-text', 'n-slots-from-entity', 'n-forms']].astype(int)
    chatbots = chatbots.sort_values(by=order_fields, ascending=[True, True, True, True, True, True, True, True, True, True, False, False, False, True])

    # Find copies (by equal fields)
    copies = chatbots[chatbots.duplicated(subset=FIELDS, keep=False)].reset_index(drop=True)
    copies.to_csv(RESULTS_FOLDER + 'copies.csv', sep=CSV_SEPARATOR, index=False)

    # Drop all copies
    chatbots.drop_duplicates(inplace=True, subset=FIELDS, keep=False)

    # Copies selection
    current_fields= pd.Series()
    copies_subgroup = []
    copies_to_keep = pd.DataFrame()
    
    for index, copy in copies.iterrows():
            
        # New row has different fields
        if not copy[FIELDS].equals(current_fields):

            # The previous subgroup is completed, ready to be checked
            if not current_fields.empty:
                    
                # Select which copies to keep (false positives and the best one of copies)
                keep_copies = select_best_copies(copies_subgroup)

                # Append copies to keep
                chatbots = pd.concat([chatbots, pd.DataFrame(keep_copies)], ignore_index=True)
                copies_to_keep = pd.concat([copies_to_keep, pd.DataFrame(keep_copies)], ignore_index=True)

                # Previous subgroup analysis completed, start with new subgroup
                current_fields = copy[FIELDS]
                copies_subgroup = [copy]

            # No previous subgroup
            else:
                copies_subgroup.append(copy)
                current_fields = copy[FIELDS] 

        # Append to previous subgroup
        else:
            copies_subgroup.append(copy)
            
    # Handle last repository
    keep_copies = select_best_copies(copies_subgroup)
    
    
    chatbots = pd.concat([chatbots, pd.DataFrame(keep_copies)], ignore_index=True)
    copies_to_keep = pd.concat([copies_to_keep, pd.DataFrame(keep_copies)], ignore_index=True)


    # Reorder dataset
    chatbots['version'] = chatbots['version'].replace('1.5', '<3.0')
    chatbots = chatbots.drop('actions-files', axis=1)
    chatbots = chatbots.sort_values(by= 'id')
    chatbots = chatbots[ORDER_COLUMNS]

    chatbots.to_csv(RESULTS_FOLDER + CHATBOT_FILE, sep=CSV_SEPARATOR, index=False)
    copies_to_keep.to_csv(RESULTS_FOLDER + 'copies_to_keep.csv', sep=CSV_SEPARATOR, index=False)
    
    



main()