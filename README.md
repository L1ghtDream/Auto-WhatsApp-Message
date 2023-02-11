# Automated WhatsApp Messages
This script allows you to send automatic messages on https://web.whatsapp.com/

## Requirements
- You must be already logged in into https://web.whatsapp.com/\-
- Python3

## Installation
### Install the dependencies
```bash
pip3 install -r requirements.txt
```
### Edit main.py
Edit these 2 line and add the phone number you want to text and the text itself
```python
# ...

number = ""
text = ""

# ...
```
### (Optional) Create a crontab entry
```bash
crontab -e

0 0 * * * pyhton3 /path/to/script/main.py # Will run every day at 00:00
```