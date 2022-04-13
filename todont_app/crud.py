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

# examples
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
# s