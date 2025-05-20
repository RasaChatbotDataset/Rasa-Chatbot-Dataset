import zipfile
import os
import re
import requests
import subprocess



# Download GitHub repository zip
def download_zip(zip_directory, repo_name, commit):
    #download_url = f"https://github.com/{repo_name}/archive/refs/heads/{branch}.zip"
    download_url =f"https://github.com/{repo_name}/archive/{commit}.zip"
    
    try: 
        response = requests.get(download_url)
        # Commit not found
        if response.status_code == 404:
            print(f'Error in repository {repo_name} ZIP download: commit {commit} not found')
            return -1
        # Generic error
        elif response.status_code != 200:
            print(f'Error in repository {repo_name} ZIP download: {response.status_code}')
            return -1
        # Commit found
        else:
            zip_path = f"{zip_directory}/{repo_name.replace('/', '_')}.zip"
            with open(zip_path, "wb") as f:
                f.write(response.content)
            return zip_path
    except requests.exceptions.Timeout:
        print(f"Timeout in repository {repo_name} ZIP download")
        return 0
    

# Delete cache and tar-gz models (except last one)
def clean_zip(zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_in:
            with zipfile.ZipFile(zip_path+'.tmp', 'w') as zip_out:
                # Select most recent model
                most_recent_model = '00000000-000000.tar.gz'
                
                for file in zip_in.namelist():
                    if file.endswith('.tar.gz'):
                        print(file)
                        # Select most recent date
                        if re.match('^\d{8}-\d{6}', file.split('/')[-1]):
                            most_recent_date = most_recent_model.split('/')[-1][:15]
                            date = file.split('/')[-1][:15]
                            if date > most_recent_date:
                                most_recent_model = file
                                
                    # Clean rasa cache
                    elif '.rasa/cache' not in file:
                        zip_out.writestr(file, zip_in.read(file))

                # Write most recent model
                if most_recent_model != '00000000-000000.tar.gz':
                    print('writing most recent')
                    zip_out.writestr(most_recent_model, zip_in.read(most_recent_model))
    
        os.remove(zip_path)
        os.rename(zip_path+'.tmp', zip_path)

    except zipfile.BadZipFile as e:
        exc_file = open('bad_zip_exception.txt', 'a', newline='')
        exc_file.write(zip_path+'\n')
        exc_file.close()


# Download and clean zip
def download_clean_zip(zip_directory, repo_name, commit):
    zip_path = download_zip(zip_directory, repo_name, commit)
    if zip_path != -1 and zip_path != 0:
        clean_zip(zip_path)


# Sync zip folder on google drive with rclone
def sync(zip_directory):
   try:
      command = ['rclone', 'sync', zip_directory, 'gdrive:'+zip_directory]
      result = subprocess.run(command, capture_output=True, text=True)
      if result.returncode == 0:
         print('Sync completed')
      else:
         print(f'Sync failed {result.sterr}')
   except Exception as e:
      print(f'Error {str(e)}')

