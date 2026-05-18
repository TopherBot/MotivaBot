# MotivaBot

MotivaBot is a tiny command‑line utility written in Python that prints a random motivational quote each time you run it. Optionally, you can supply a Telegram bot token and chat ID to have the quote sent directly to a Telegram chat.

## Features
- Zero‑dependency: uses only the Python standard library.
- Instant scaffolding: just `python motibot.py`.
- Quick CI‑ready: the repository includes a minimal GitHub Actions workflow (you can add it later).

## Usage
```bash
python motibot.py               # prints a quote to stdout
python motibot.py --telegram BOT_TOKEN CHAT_ID   # also sends to Telegram
```

## Adding to CI
You can create a `.github/workflows/ci.yml` that runs `python -m unittest` if you add tests later.

## License
MIT – see LICENSE file (add later if you wish).