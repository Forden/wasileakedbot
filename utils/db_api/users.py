from aiogram import types

import models
from .consts import RawConnection


class BotUsers(RawConnection):
    @staticmethod
    async def get_user_data(user_id: int) -> models.BotUser:
        sql = 'SELECT * FROM bot_users WHERE user_id = %s'
        params = (user_id,)
        return await BotUsers._make_request(sql, params, fetch=True, model_type=models.BotUser)

    @staticmethod
    async def register(user: types.User):
        if not (await BotUsers.get_user_data(user.id)):
            sql = 'INSERT INTO bot_users (user_id, name) VALUES (%s, %s)'
            params = (user.id, user.full_name)
            await BotUsers._make_request(sql, params)
