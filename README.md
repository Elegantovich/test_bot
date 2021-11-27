# test_bot
### Описание
- Телеграмм бот, помогающий выбрать пиццу
- Тестирование производится посредством использования Client API:
необходимо ввести свой api_id, api_hash. Получить все это можной по ссылке
https://my.telegram.org/
### Технологии
- Python 3.9.9, python-telegram-bot 13.8.1, Pyrogram 1.2.9
### Запуск проекта dev-режиме
- Установите и запустите виртуальное окружение
```
python -m venv venv 
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python3 bot.py
``` 
- Для тестирование диалога с ботом выполните команду:
```
python3 test_bot.py
```
- Ссылка на схему стейт машины
```
https://github.com/Elegantovich/test_bot/blob/Elegantovich/state%20machine.png
```
![alt text](https://github.com/Elegantovich/test_bot/blob/Elegantovich/state%20machine.png)
