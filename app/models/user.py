from sqlalchemy import Column,Integer,String,Boolean,ForeignKey 
from app.db.database import Base 

class User(Base):
    __tablename__ = "user"