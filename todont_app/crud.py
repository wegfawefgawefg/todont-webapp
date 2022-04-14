from sqlalchemy.orm import Session

from . import models, schemas

# get all todonts
def get_todonts(db: Session):
    return db.query(models.ToDont).all()

# get a todont by id
def get_todont(db: Session, todont_id: int):
    return db.query(models.ToDont).filter(models.ToDont.id == todont_id).first()

# set a todont to done
def set_done(db: Session, todont_id: int):
    todont = get_todont(db, todont_id)
    if todont:
        todont.done = True
    return todont

# create a todont
def create_todont(db: Session, todont: schemas.ToDontCreate):
    db_todont = models.ToDont(
        description=todont.description,
        done=False
    )
    db.add(db_todont)
    db.commit()
    db.refresh(db_todont)
    return db_todont
