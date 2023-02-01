from aiogram import executor
from handlers import dp
from config import TOKEN


async def on_startup(_):
  print('bot запущен')

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
  #executer вызывает метод старт поллинг, т.е он слушает- отлавилиявает наши сообщения
  #skip_updates=True если Тру, то пропускает все сообщения , когда бот был неактивен
  #skip_updates=False, если Фолс, то после включения повалятся ответы на все сообщения
  #on_startup=on_startup запускаем нашу функцию "бот запущен"

