from aiogram import types

from utils import db_api


async def bot_start(msg: types.Message):
    m = [
        f'Привет, {msg.from_user.full_name}!',
        'Этот бот поможет проверить, утекли ли твои (или твоего друга) данные.\n',
        'Введите ID человека, которого нужно проверить',
        'Пример: <code>123</code>',
        'Получить ID можно с помощью @my_id_bot'
    ]
    await msg.answer('\n'.join(m))
    await db_api.BotUsers.register(msg.from_user)
