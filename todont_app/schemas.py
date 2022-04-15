from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ToDontBase(BaseModel):
    description: str

class ToDontCreate(ToDontBase):
    pass

class ToDont(ToDontBase):
    id: int
    created_ts: datetime
    done: bool = False

    class Config:
        orm_mode = True
