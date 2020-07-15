from config import telegram_key
from telegram.ext import *
import requests

help_text = '''
Все команды бота:

/help - Вывести все команды
/get_time {Номер города}
1. Ульяновск
2. Москва
3. Нью-Йорк
4. Лондон
'''


def get_time_handle(update, context):
    if len(update.message.text.split(' ')) == 1:
        numCity = "1"
    else:
        numCity = update.message.text.split(' ')[1]

    time = ""
    if numCity == "1":
        time = "Время в Ульяновске: " + requests.get('http://worldtimeapi.org/api/timezone/Europe/Ulyanovsk').json()[
            "datetime"].split('T')[1].split('.')[0]
    elif numCity == "2":
        time = "Время в Москве: " + requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow').json()[
            "datetime"].split('T')[1].split('.')[0]
    elif numCity == "3":
        time = "Время в Нью-Йорке: " + requests.get('http://worldtimeapi.org/api/timezone/America/New_York').json()[
            "datetime"].split('T')[1].split('.')[0]
    elif numCity == "4":
        time = "Время в Лондоне: " + requests.get('http://worldtimeapi.org/api/timezone/Europe/London').json()[
            "datetime"].split('T')[1].split('.')[0]
    else:
        time = "Нет такого пункта в списке городов"

    update.message.reply_text(time)


def help_handle(update, context):
    update.message.reply_text(help_text)


def start_handle(update, context):
    update.message.reply_text('Привет! Этот бот показывает время в городе' + help_text)


def any_message(update, context):
    update.message.reply_text("Команда не поддерживается\n\n" + help_text)


def main():
    updater = Updater(telegram_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help", help_handle))
    dp.add_handler(CommandHandler("start", start_handle))
    dp.add_handler(CommandHandler("get_time", get_time_handle))
    dp.add_handler(MessageHandler(Filters.text, any_message))
    updater.start_polling()


if __name__ == '__main__':
    main()
