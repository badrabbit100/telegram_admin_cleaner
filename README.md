# Telegram Bot - Cleaner Messages

### Description
This Telegram-Bot clean service messages from telegram group
From example message like: 
"user join the group" or "user left the group"

### Installation

- Clone Repository
```
git clone https://github.com/badrabbit100/telegram_admin_cleaner.git
```
- Create virtual environment, install modules from requirements.txt
```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

- This code request sensitive data from the .env file.
```
nano .env
```
- Add data to the .env file 

> Api_ID, Api_HASH - you can get from [my.telegram.org](https://my.telegram.org)
> 
> All data add to the file without " "
```
API_ID=11111111
API_HASH=asdasdasdasdasdasdasad
SESSION_ID=AnyNameOfSession
CHANNEL_NAME=channel_name
```
- Start Application
```
python3 main.py
```
### Support
Telegram [@TonyFreeSec](https://t.me/tonyfreesec) 