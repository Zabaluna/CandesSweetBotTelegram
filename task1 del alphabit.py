# ## Групповая работа [2]

# Учимся настраивать виртуальное окружение и работать с [PIP](https://pypi.org/)

# В качестве пробы библиотек к программам предыдущего модуля подключить работу с XML \ JSON

# > Для тренировки можно создания телеграм-бота полезные ссылки:
# > 
# > 
# > [https://core.telegram.org/bots](https://core.telegram.org/bots)
# > 
# > [https://github.com/python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
# > 
# > [https://core.telegram.org/bots/api#authorizing-your-bot](https://core.telegram.org/bots/api#authorizing-your-bot)
# > 
# > [https://core.telegram.org/bots/api#available-methods](https://core.telegram.org/bots/api#available-methods)
# > 
# > [https://core.telegram.org/bots/api#user](https://core.telegram.org/bots/api#user)
# > 

# **Задача:** при помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 2. Создайте программу для игры с конфетами человек против человека.
    
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    
#     a) Добавьте игру против бота
    
#     b) Подумайте как наделить бота "интеллектом"

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
from telegram.ext import MessageHandler, filters


async def text_changer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    txt = update.message.text
    await update.message.reply_text(' '.join(list(filter(lambda element: 'при' not in element.lower(), txt.split()))))


app = ApplicationBuilder().token("TOKEN").build()


app.add_handler(MessageHandler(filters.TEXT, text_changer))



print('start')
app.run_polling()