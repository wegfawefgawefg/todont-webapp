from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class ToDont(Base):
    __tablename__ = "todont"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    done = Column(Boolean, default=False)