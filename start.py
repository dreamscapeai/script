import os
import subprocess

# URL of the GitHub repository
repo_url = 'https://github.com/dreamscapeai/SGMSL'

# Local directory to clone the repository into
local_dir = os.path.expanduser('~/.dreamscapeai')

# Function to clone the repository directly into the specified directory
def clone_repo_directly(repo_url, local_dir):
    try:
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        # Change the current working directory to the target directory
        os.chdir(local_dir)
        # Clone the repository into the current directory
        subprocess.run(['git', 'clone', repo_url, '.'], check=True)
        print(f"Repository cloned successfully to {local_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning the repository: {e}")
    except IOError as e:
        print(f"Error creating the directory {local_dir}: {e}")

# Clone the repository
clone_repo_directly(repo_url, local_dir)
