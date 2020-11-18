from twilio.rest import Client
import time
import requests

with open('auth.txt', 'r') as txt:
    f = txt.read().split()
    acc_sid = f[0]
    token = f[1]


def joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    response = response.json()
    setup = response['setup']
    punchline = response['punchline']
    joke = ['Next one >', setup, punchline, ]
    account_sid = acc_sid
    auth_token = token
    client = Client(account_sid, auth_token)

    for text in joke:
        time.sleep(5)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=text,
            to='whatsapp:+918949266322'
        )


# print(message.sid)
