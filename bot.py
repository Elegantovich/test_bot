import datetime as dt
import logging
import os

from telegram.ext import CommandHandler, MessageHandler, Updater, Filters
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TELEGRAM_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def hello_time(hours):
    "Приветствие в зависимости от часа."
    if hours in range(6, 12):
        return 'Доброе утро'
    elif hours in range(12, 18):
        return 'Добрый день'
    elif hours in range(18, 23):
        return 'Добрый вечер'
    return 'Доброй ночи'


def wake_up(update, context):
    "Ответ на команду /start."
    hours_now = int(dt.datetime.now().strftime('%H'))
    chat = update.effective_chat
    name = update.message.chat.first_name

    context.bot.send_message(
        chat_id=chat.id,
        text=f'{hello_time(hours_now)}, {name}!'
    )
    context.bot.send_message(
        chat_id=chat.id,
        text='Какую вы хотите пиццу? Большую или маленькую?'
    )


def get_text(update, context):
    "Функция обработчик постапающих текстовых запросов."
    chat = update.effective_chat

    if update.message.text in ['Большую', 'большую']:
        context.bot.send_message(
            chat_id=chat.id,
            text='Как вы будете платить?')
    elif update.message.text in ['Наличкой', 'наличкой']:
        context.bot.send_message(
            chat_id=chat.id,
            text='Вы хотите большую пиццу, оплата - наличкой?')
    elif update.message.text in ['Да', 'да']:
        context.bot.send_message(
            chat_id=chat.id,
            text='Спасибо за заказ')
    elif update.message.text in ['Нет', 'нет']:
        context.bot.send_message(
            chat_id=chat.id,
            text='Досвидания')
    else:
        context.bot.send_message(chat_id=chat.id,
                                 text='Пожалуйста, выражайтесь яснее!')


def main():
    updater = Updater(token=token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, get_text))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
