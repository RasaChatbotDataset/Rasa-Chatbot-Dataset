import zipfile
import ast
import os
import pandas as pd
from difflib import SequenceMatcher
import argparse


RESULTS_FOLDER = os.path.join('results', '14_results')
INPUT_FOLDER = os.path.join('results', '13_results')
CHATBOT_FILE = 'chatbots.csv'
CSV_SEPARATOR= ';'
ZIP_FOLDER = 'chatbot_repositories_zip'
DATE_FILES = [os.path.join('results', '06_results', 'chatbots_sfsd.csv'), os.path.join('results', '06_results', 'chatbots_mfsd.csv'), os.path.join('results', '06_results', 'chatbots_sfmd.csv'), os.path.join('results', '06_results', 'chatbots_mfmd.csv')]
FIELDS = ['intents', 'entities', 'actions', 'slots','slots-type', 'forms', 'config-languages', 'training-language', 'response-languages', 'n-actions-files']

ORDER_COLUMNS = ['id', 'full-name', 'html-url', 'stars', 'forks', 'owner-name', 'owner-type', 'created-at', 'last-commit', 'last-commit-date', 'domain-files', 'type', 'n-intents', 'intents', 'n-entities', 'entities', 'n-actions', 'actions', 'n-actions-custom', 'actions-custom', 'n-slots', 'slots', 'n-slots-from-entity', 'n-slots-from-text', 'slots-type', 'n-forms', 'forms', 'version', 'config-languages', 'training-language', 'response-languages', 'languages', 'has-english', 'pure-english', 'n-actions-files']

# Keep only the best copies
def select_best_copies(copies):

    # The first copy is the best one based on our sorting
    best_copies = []
    diff_action_files_set = []

    # No action file: keep only best one
    if copies[0]['n-actions-files'] == 0:
        best_copies = [copies[0]]

    # Action files
    else:
        for copy in copies:

            copy_action_files_contents = []

            # Open zip
            zip_path = os.path.join(ZIP_FOLDER, copy['full-name'].replace('/', '_') + '.zip')
            try:
                repository =  zipfile.ZipFile(zip_path, 'r')
            except:
                print(copy['full-name'])
                return
        
            # Extract all action files content and save them in alphabetical order
            action_files = ast.literal_eval(copy['actions-files'])
            for action_file in action_files:
            
                full_action_path = copy['full-name'].split('/')[-1]+'-'+copy['last-commit']+ '/' + action_file
                with repository.open(full_action_path) as d_file:
                    try:
                        # Decode file content
                        content = d_file.read().decode()
                        clean_content = ''.join(content.split())

                        # Add content
                        copy_action_files_contents.append(clean_content)

                    except Exception as e:
                        print(f"Decode error for {copy['id']}")
                        print(e)
                        continue

            # Sort action files contents            
            copy_action_files_contents.sort()

            if not diff_action_files_set:
                diff_action_files_set.append(copy_action_files_contents)
                best_copies.append(copy)
                continue
                        
            # Verify copy's action files similarity with actions files of other copies already saved
            is_new = True
            # For each set of files (files of a copy) saved
            for contents_set in diff_action_files_set:

                all_files_same = True
                # For each file  in the current copy set
                for copy_file in copy_action_files_contents:
                    found_copy = False
                    # For each file in the saved files set
                    for saved_file in contents_set:
                        # If the file matches with the file of the considered save set
                        if SequenceMatcher(None, saved_file, copy_file).ratio() >= 0.95:
                            found_copy = True
                            break
                    all_files_same = all_files_same and found_copy
                    # file not found in considered saved set: check new set
                    if not found_copy:
                        break
                # If we found a copy of each file in a file set already saved: chatbot is a copy
                if all_files_same:
                    is_new = False
                    break

            # If chatbot new save its file files set
            if is_new:
                diff_action_files_set.append(copy_action_files_contents)
                best_copies.append(copy)
            
            repository.close()


    return best_copies


# Update version of chatbot not updated after Rasa 2
def update_version(chatbot):
    if isinstance(chatbot['last-commit-date'], str) and chatbot['last-commit-date'][0:10] < '2020-10-07' and pd.isna(chatbot['version']):
        print('change')
        chatbot['version'] = '1.0'
    if not isinstance(chatbot['last-commit-date'], str):
        print(chatbot['last-commit-date'])
    return chatbot


def main():

    # Create result folder
    if not os.path.isdir(RESULTS_FOLDER):
        os.mkdir(RESULTS_FOLDER)

    # Optional argument for number of chatbots
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument(
        "--n-chatbots",
        type=int,
        default=-1,
        help="Number of chatbots (default: all)"
    )

    args = parser.parse_args()

    print('\n\n', '-'*20, 'DUPLICATE CHATBOTS REMOVAL', '-'*20, '\n') 

    # Open files
    chatbots= pd.read_csv(os.path.join(INPUT_FOLDER, CHATBOT_FILE), sep=CSV_SEPARATOR)

    # Chatbot number check
    if args.n_chatbots >0 and args.n_chatbots < chatbots.shape[0]:
        chatbots = chatbots.head(args.n_chatbots)
        print(f'Number of chatbots: {args.n_chatbots}\n')
    else:
        print(f'Number of chatbots: {chatbots.shape[0]} (all)\n')

    # Join with relevant fields
    cb_files = pd.DataFrame()
    for file in DATE_FILES:
        cb_with_files = pd.read_csv(file, sep=CSV_SEPARATOR)
        cb_with_files = cb_with_files[['id', 'created-at', 'owner-name', 'owner-type', 'last-commit-date', 'actions-files']]
        cb_files = pd.concat([cb_files, cb_with_files])
    chatbots = pd.merge(chatbots, cb_files, how='inner', on=['id'])
    chatbots.to_csv(os.path.join(RESULTS_FOLDER, 'chatbots_join_date.csv'), sep=CSV_SEPARATOR, index=False)
    
    # Order chatbots to have copies one after another
    order_fields = FIELDS + ['version', 'stars', 'forks', 'created-at'] 
    chatbots[['n-entities', 'n-slots', 'n-slots-from-text', 'n-slots-from-entity', 'n-forms']] = chatbots[['n-entities', 'n-slots', 'n-slots-from-text', 'n-slots-from-entity', 'n-forms']].astype(int)
    chatbots = chatbots.sort_values(by=order_fields, ascending=[True, True, True, True, True, True, True, True, True, True, False, False, False, True])

    # Find copies (by equal fields)
    copies = chatbots[chatbots.duplicated(subset=FIELDS, keep=False)].reset_index(drop=True)

    # Copies found
    if not copies.empty:

        copies.to_csv(os.path.join(RESULTS_FOLDER, 'copies.csv'), sep=CSV_SEPARATOR, index=False)

        # Drop all copies
        chatbots.drop_duplicates(inplace=True, subset=FIELDS, keep=False)

        # Copies selection
        current_fields= pd.Series()
        copies_subgroup = []
        copies_to_keep = pd.DataFrame()
        
        for index, copy in copies.iterrows():

            if index%50 == 0:
                print(f'> Processed chatbots: {index}/{chatbots.shape[0]}')
                
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

    print(f'> Processed chatbots: {chatbots.shape[0]}/{chatbots.shape[0]}\n')

    if not copies.empty:
        print('Best copies selection: started')    
        # Handle last repository
        keep_copies = select_best_copies(copies_subgroup)
        print('Best copies selection: started')  
        in_chatbots = chatbots.shape[0]
        
        
        chatbots = pd.concat([chatbots, pd.DataFrame(keep_copies)], ignore_index=True)
        copies_to_keep = pd.concat([copies_to_keep, pd.DataFrame(keep_copies)], ignore_index=True)

    # Reorder dataset
    chatbots = chatbots.apply(update_version, axis=1)
    chatbots = chatbots.drop('actions-files', axis=1)
    chatbots = chatbots.sort_values(by= 'id')
    chatbots = chatbots[ORDER_COLUMNS]

    chatbots.to_csv(os.path.join(RESULTS_FOLDER, CHATBOT_FILE), sep=CSV_SEPARATOR, index=False)
    print('Step 14 completed')

    if not copies.empty:
        copies_to_keep.to_csv(os.path.join(RESULTS_FOLDER, 'copies_to_keep.csv'), sep=CSV_SEPARATOR, index=False)
        fn_chatbots = chatbots.shape[0]
        print(f'COPIES DELETED: {fn_chatbots - in_chatbots}\n')
    else:
        print('NO COPIES FOUND\n')

    print('CONGRATULATIONS: YOUR TOFU-R IS READY')


main()