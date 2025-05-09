import telegram
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

bot = telegram.Bot(token=config['telegram']['token'])
chat_id = config['telegram']['chat_id']

def notify(message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Telegramga yuborishda xatolik: {e}")

