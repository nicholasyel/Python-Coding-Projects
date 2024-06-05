import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : '2018033831',
        'message' : 'Hey, whats up Andrey!',
        'key' : 'textbelt'
    })
    print(resp.json())

#schedule.every().day.at('10:00').do(send_message)