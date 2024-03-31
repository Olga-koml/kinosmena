import requests
import telegram
from django.conf import settings

# bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)


class BotError(Exception):
    pass


# def send_message(message, telegram_id):
#     """Отправка отчета в Telegram чат."""
#     bot = telegram.Bot(token=settings.BOT_TOKEN)
#     try:
#         bot.send_message(telegram_id, message)
#     except telegram.TelegramError as error:
#         raise BotError(f'Не удалось отправить отчет {error}')

   
# эту функцию не удалось подключить. 
async def send_message_async(message, telegram_id):
    """Отправка отчета в Telegram чат."""
    bot = telegram.Bot(token=settings.BOT_TOKEN)
    try:
        await bot.send_message(telegram_id, message)
    except Exception as error:
        raise BotError(f'Не удалось отправить отчет {error}')
    
# сейчас шлет сообщение в ТГ эта функция
def send_telegram_message(chat_id, message):
    bot_token = settings.BOT_TOKEN
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, params=params)
    return response.json()