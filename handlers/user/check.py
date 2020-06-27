from aiogram import types

from utils import db_api


async def check(msg: types.Message):
    user_id = None
    if msg.text.isdigit():
        user_id = int(msg.text)
    if msg.forward_from and msg.forward_from.id:
        user_id = msg.forward_from.id
    if user_id:
        userdata = await db_api.LeakedUsers.get_user_data(user_id)
        if userdata:
            if msg.from_user.id == user_id:
                m = [
                    'Ваш профиль найден в базе данных. Ниже приведены все известные данные:',
                    f'Имя: {userdata.name}',
                    f'Фамилия: {userdata.fname}',
                    f'Номер телефона: {userdata.phone}',
                    f'Юзернейм: @{userdata.nik}',
                    f'Номер в БД: <code>{userdata.row_id}</code>',
                ]
            else:
                m = [
                    f'Профиль пользователя <code>{user_id}</code> найден в БД. Номер оканчивается на {str(userdata.phone)[-2:]}'
                ]
        else:
            m = [f'Профиль пользователя <code>{user_id}</code> не найден в БД']
    else:
        m = ['Пришлите ID человека или перешлите его сообщение']
    await msg.reply('\n'.join(m))
