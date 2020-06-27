from pydantic import BaseModel


class LeakedUser(BaseModel):
    row_id: int
    name: str
    fname: str
    phone: int
    uid: int
    nik: str
    wo: str
