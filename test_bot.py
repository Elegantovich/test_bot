import time
import os

from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = Client('my_account', api_id, api_hash)
error_message = 'Ошибка, ответ не совпадает с ожидаемым!'


def test_bot():
    """Проверяем реальный ответ с ожидаемым."""
    client.start()
    client.send_message('pizza_teststs_bot', '/start')
    time.sleep(1)
    message = client.get_history('pizza_teststs_bot', limit=1)
    message = message[0]["text"]
    assert message == 'Какую вы хотите пиццу? Большую или маленькую?', (
        error_message)

    client.send_message('pizza_teststs_bot', 'Большую')
    time.sleep(1)
    message = client.get_history('pizza_teststs_bot', limit=1)
    message = message[0]["text"]
    assert message == 'Как вы будете платить?', error_message

    client.send_message('pizza_teststs_bot', 'Наличкой')
    time.sleep(1)
    message = client.get_history('pizza_teststs_bot', limit=1)
    message = message[0]["text"]
    assert message == 'Вы хотите большую пиццу, оплата - наличкой?', (
        error_message)

    client.send_message('pizza_teststs_bot', 'Да')
    time.sleep(1)
    message = client.get_history('pizza_teststs_bot', limit=1)
    message = message[0]["text"]
    assert message == 'Спасибо за заказ', error_message
    client.stop()


def main():
    test_bot()


if __name__ == '__main__':
    main()
