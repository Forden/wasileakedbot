from pydantic import BaseModel


class DBStats(BaseModel):
    min_id: int
    max_id: int
    total: int
