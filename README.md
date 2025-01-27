# Auto commit
## For the code to work properly you need to set up your GH credentials:
```
sudo git config --system user.email "you@example.com"
sudo git config --system user.name "Your Name"
``` 
- Run the `main.py` once to put in your `github_token` or create `.github_token` in your home directory.
- Create a text file `folder_to_check.txt` to place in all your folders.
- Run `setup_cron.sh` to create a cron job.
- Run `remove_cron.sh` to remove the cron job.
