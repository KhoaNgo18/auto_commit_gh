SCRIPT_PATH="/home/ubuntu/khoa/others/auto_commit_gh/main.py"
crontab -l | grep -v "python3 $SCRIPT_PATH" | crontab -
