import os
import requests

# List of file URLs in the GitHub subfolder
file_urls = [
    'https://github.com/dreamscapeai/script/blob/main/SGM/conda.py',
    'https://github.com/dreamscapeai/script/blob/main/SGM/cleanup.py',
    'https://github.com/dreamscapeai/script/blob/main/SGM/comfyui.py',
    'https://github.com/dreamscapeai/script/blob/main/SGM/a1111.py'
]

# Local directory to save the files
local_dir = os.path.expanduser('~/.dreamscapeai')

# Create the directory if it doesn't exist
os.makedirs(local_dir, exist_ok=True)

# Function to download a file
def download_file(url, local_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully to {local_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file from {url}: {e}")
    except IOError as e:
        print(f"Error writing the file to {local_path}: {e}")

# Download each file
for file_url in file_urls:
    file_name = os.path.basename(file_url)
    local_path = os.path.join(local_dir, file_name)
    download_file(file_url, local_path)

print("All files have been downloaded and moved to
