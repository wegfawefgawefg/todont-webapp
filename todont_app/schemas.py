from datetime import datetime
from pydantic import BaseModel

class Todont(BaseModel):
    id: int
    description: str
    created_ts: datetime
    done: bool = False

    class Config:
        orm_mode = True

class TodontCreate(Todont):
    description: str


"""
wtf is the difference between base, the model and the create model?
https://fastapi.tiangolo.com/tutorial/sql-databases/#create-pydantic-models-schemas-for-reading-returning
"""