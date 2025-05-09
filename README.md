# Realized Profit Copy Trading Bot

This bot copies trades from a master MT5 account to multiple slave accounts in real time.

## Setup

1. Install Python dependencies:
```
pip install -r requirements.txt
```

2. Edit `config.yaml` with your MT5 account details and paths.

3. Ensure each MT5 terminal is installed at the given `path` in `config.yaml`.

4. Run the bot:
```
python main.py
```

## How it works

- `main.py` loads configuration and initializes MT5Connector.
- `mt5_connector.py` handles connections to master and slave accounts.
- `copy_logic.py` continuously monitors master positions and opens/closes positions on slaves.
