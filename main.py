import os
import subprocess
from pathlib import Path
from datetime import datetime

def check_github_login(token_file):
    """Check if GitHub login information exists. If not, prompt for a token and save it."""
    if not token_file.exists():
        print("GitHub is not logged in.")
        token = input("Enter your GitHub Personal Access Token: ").strip()
        token_file.write_text(token)
        print("Token saved for future use.")
    else:
        print("GitHub token found.")

def git_status(folder_path):
    """Check if there are changes in the git repository at the specified folder path."""
    os.chdir(folder_path)
    result = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip() != ""

def git_add_commit_push():
    """Add, commit, and push changes to the repository."""
    subprocess.run(["git", "add", "-A"])
    date = datetime.now().strftime("%d/%m/%Y")
    commit_message = f"Changed in date: {date}"
    subprocess.run(["git", "commit", "-m", commit_message])
    
    # Explicitly set the environment variable for token-based authentication
    subprocess.run(["git", "push"], env={**os.environ, "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")})

def main():
    # Define the path to the token file
    home = Path.home()
    token_file = home / ".github_token"

    # Define the path to the folder to check
    folder_file = home / "folder_to_check.txt"

    if not folder_file.exists():
        print("Folder path file not found. Please create a file named 'folder_to_check.txt' in your home directory with the folder path to monitor.")
        return

    folder_path = folder_file.read_text().strip()

    if not Path(folder_path).exists():
        print(f"The folder path '{folder_path}' does not exist. Please check the path in 'folder_to_check.txt'.")
        return

    # Check GitHub login
    check_github_login(token_file)

    # Export the token as an environment variable for Git
    token = token_file.read_text().strip()
    os.environ["GITHUB_TOKEN"] = token

    # Check git status
    if git_status(folder_path):
        print("Changes detected. Preparing to commit...")
        git_add_commit_push()
    else:
        print("No changes detected.")

if __name__ == "__main__":
    main()
