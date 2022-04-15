from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

from .database import Base

class ToDont(Base):
    __tablename__ = "todont"

    id = Column(Integer, primary_key=True, index=True)
    created_ts = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    # created_ts = Column(DateTime)
    # updated_ts = Column(Datetime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    description = Column(String)
    done = Column(Boolean, default=False)