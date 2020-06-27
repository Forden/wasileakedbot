from typing import Optional

import models
from .consts import RawConnection


class LeakedUsers(RawConnection):
    @staticmethod
    async def get_user_data(user_id: int) -> Optional[models.LeakedUser]:
        sql = 'SELECT * FROM users WHERE uid = %s'
        params = (user_id,)
        return await LeakedUsers._make_request(sql, params, fetch=True, model_type=models.LeakedUser)

    @staticmethod
    async def get_stats() -> models.DBStats:
        sql = 'SELECT min(uid) as min_id, max(uid) as max_id, count(*) as total FROM users'
        return await LeakedUsers._make_request(sql, fetch=True, model_type=models.DBStats)
