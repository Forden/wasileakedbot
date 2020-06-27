from aiogram import types

from utils import db_api


async def get_stats(msg: types.Message):
    stats = await db_api.LeakedUsers.get_stats()
    m = [
        f'Записей в БД: {stats["res"]}',
        f'Минимальный ID: {stats["minn"]}',
        f'Максимальный ID: {stats["maxx"]}'
    ]
    await msg.reply('\n'.join(m))

