import os
import subprocess

# URL of the GitHub repository
repo_url = 'https://github.com/dreamscapeai/SGMSL'

# Local directory to clone the repository into
local_dir = os.path.expanduser('~/.dreamscapeai')

# Function to clone the repository
def clone_repo(repo_url, local_dir):
    try:
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        subprocess.run(['git', 'clone', repo_url, local_dir], check=True)
        print(f"Repository cloned successfully to {local_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning the repository: {e}")
    except IOError as e:
        print(f"Error creating the directory {local_dir}: {e}")

# Clone the repository
clone_repo(repo_url, local_dir)
