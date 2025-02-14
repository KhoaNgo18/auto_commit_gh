#!/bin/bash

# Path to the Python script
SCRIPT_PATH="/home/khoa/Khoa/my-project/auto-commit-github/main.py"
HOUR=22
MINUTE=00
# Cron job command
CRON_JOB="$MINUTE $HOUR * * * python3 $SCRIPT_PATH > auto_commit.log 2>&1"

(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
echo "Cron job has been added to run daily at $HOUR:$MINUTE."

##
HOUR=21
MINUTE=55
# Cron job command
CRON_JOB="$MINUTE $HOUR * * * git pull"

(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
echo "Cron job has been added to run daily at $HOUR:$MINUTE."