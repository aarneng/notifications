from dotenv import load_dotenv
import os
import requests


def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Failed to send message. Status code: {response.status_code}")
    else:
        print("Message sent successfully!")


load_dotenv()

chat_id = os.getenv("CHAT_ID")
bot_token = os.getenv("BOT_ID")

message = "This is a test message sent from my Python script!"

send_telegram_message(bot_token, chat_id, message)
