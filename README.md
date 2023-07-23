
# TeleSalesDataBot

Author: $Kek - MrStarXCODE

Date: 2023-07-23

## Description

TeleSalesDataBot is a Telegram bot designed to collect sales data in an e-commerce setting. The bot prompts the user to input details about a sale, including the product name, price, hash, buyer username/email, and a note. This information is then stored in an Excel file, with each sale recorded on a new row. The Excel file is formatted for readability, with autofitted columns.

## Installation

This project requires Python 3 and the following Python libraries installed:

- [python-telegram-bot](https://python-telegram-bot.org/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

You can install these packages using pip:

```bash
pip install python-telegram-bot pandas openpyxl
```

## How to Run

1. Replace `'YOUR_BOT_TOKEN'` in the code with your actual bot token from the Telegram BotFather.
2. Run the Python script on a server. The bot will then be live and can be interacted with on Telegram.
3. Initiate a chat with the bot and use the `/start` command to start inputting sales data.
4. The bot will prompt you for each piece of information, one at a time.
5. If at any point you wish to cancel the operation, use the `/cancel` command.

## Usage

Please note that this bot is currently configured to only accept input from the user with ID 2020220. This can be adjusted in the code if desired.

Also, remember to always keep your bot token secret and never share it with anyone you do not trust. Anyone with your bot token can control your bot.

## License

This project is for personal use. Please do not distribute or use this code for commercial purposes without consent.

