#!/usr/bin/env python3
"""MotivaBot – print a random motivational quote, optionally send to Telegram.

Usage:
  python motibot.py               # prints a quote
  python motibot.py --telegram <TOKEN> <CHAT_ID>

The script is self‑contained and requires only the Python standard library.
"""
import argparse
import json
import random
import sys
import urllib.request

QUOTES = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "The future belongs to those who prepare for it today. – Malcolm X",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
]

def get_random_quote():
    return random.choice(QUOTES)

def send_telegram(token, chat_id, text):
    # Telegram Bot API sendMessage method
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({"chat_id": chat_id, "text": text}).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            resp_data = resp.read().decode('utf-8')
            result = json.loads(resp_data)
            if not result.get('ok'):
                raise RuntimeError(f"Telegram API error: {result}")
    except Exception as e:
        print(f"Failed to send Telegram message: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='MotivaBot – random quote generator')
    parser.add_argument('--telegram', nargs=2, metavar=('TOKEN', 'CHAT_ID'), help='Send quote to Telegram')
    args = parser.parse_args()

    quote = get_random_quote()
    print(quote)
    if args.telegram:
        token, chat_id = args.telegram
        send_telegram(token, chat_id, quote)

if __name__ == "__main__":
    main()
