from datetime import datetime

from pydantic import BaseModel


class BotUser(BaseModel):
    user_id: int
    name: str
    reg_time: datetime
