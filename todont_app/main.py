from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todonts/", response_model=schemas.ToDont)
async def create_todont(todont: schemas.ToDontCreate, db: Session = Depends(get_db)):
    return crud.create_todont(db=db, todont=todont)

@app.get("/todonts/", response_model=List[schemas.ToDont])
def read_todonts(db: Session = Depends(get_db)):
    return crud.get_todonts(db)

@app.put("/todonts/{todont_id}/done/", response_model=schemas.ToDont)
def set_done(todont_id: int, db: Session = Depends(get_db)):
    todont = crud.get_todont(db, todont_id)
    if not todont:
        raise HTTPException(status_code=404, detail="ToDont not found")
    return crud.set_done(db, todont_id)