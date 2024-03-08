# whatsapp_joke

Automate sending jokes to your WhatsApp using Twilio's API. This Python script fetches a random joke from the [Official Joke API](https://official-joke-api.appspot.com/) and sends it to a specified WhatsApp number.

## Prerequisites
1. Python installed on your system.
2. Required Python packages installed. You can install them using the following command:

```bash
pip install twilio requests
```

## Configuration
1. Create a file named `auth.txt` with the following information:
   - Line 1: Twilio Account SID
   - Line 2: Twilio Auth Token
   - Line 3: Your WhatsApp number

2. Save your `auth.txt` file.

## Usage
Run the script using the following command:

```bash
python script_name.py
```

The script will send a sequence of WhatsApp messages with a random joke (including setup and punchline) to the specified number.

Feel free to customize the script according to your needs.