from aiogram import types

from utils import db_api


async def get_stats(msg: types.Message):
    stats = await db_api.LeakedUsers.get_stats()
    m = [
        f'Записей в БД: {stats.total}',
        f'Минимальный ID: {stats.min_id}',
        f'Максимальный ID: {stats.max_id}'
    ]
    await msg.reply('\n'.join(m))
