from typing import Dict

import models
from .consts import RawConnection


class LeakedUsers(RawConnection):
    @staticmethod
    async def get_user_data(user_id: int) -> models.LeakedUser:
        sql = 'SELECT * FROM users WHERE uid = %s'
        params = (user_id,)
        return await LeakedUsers._make_request(sql, params, fetch=True, model_type=models.LeakedUser)

    @staticmethod
    async def get_stats() -> Dict[str, int]:
        sql = 'SELECT min(uid) as minn, max(uid) as maxx, count(*) as res FROM users'
        return await LeakedUsers._make_request(sql, fetch=True)
