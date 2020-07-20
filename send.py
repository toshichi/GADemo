#!/usr/bin/env python3
import os
import requests
import sys

def push(bot_token, chat_id, text):
    url = "https://api.telegram.org/bot%s/sendMessage" % bot_token

    payload = {
        "text": text,
        "chat_id": chat_id,
        "parse_mode": "Markdown"
    }
    return requests.post(url, data=payload, timeout=10).text

if __name__ == "__main__":
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    if bot_token and chat_id:
        print(push(bot_token, chat_id, sys.argv[1]))
    else:
        print("Token not set, exiting.")