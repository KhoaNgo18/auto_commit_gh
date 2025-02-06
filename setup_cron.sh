#!/bin/bash

# Path to the Python script
SCRIPT_PATH="/home/ubuntu/khoa/others/auto_commit_gh/main.py"
HOUR=20
MINUTE=00
# Cron job command
CRON_JOB="$MINUTE $HOUR * * * python3 $SCRIPT_PATH > auto_commit.log 2>&1"

# Check existing cron jobs
(crontab -l 2>/dev/null || true) | grep -q "$CRON_JOB"
if [ $? -eq 0 ]; then
    echo "Cron job is already set."
else
    # Add the cron job
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "Cron job has been added to run daily at $HOUR:$MINUTE."
fi
