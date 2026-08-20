from sqlalchemy import Column,Integer,Boolean,VARCHAR,DateTime
from app.db.database import Base 
from datetime import datetime,timezone 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(VARCHAR(255), unique=True, index=True, nullable=False)
    hashed_password = Column(VARCHAR(255), nullable=False)
    full_name = Column(VARCHAR(255),nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(VARCHAR(100),default="USER")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),nullable=False)

    owned_projects = relationship("ResearchProject", back_populates="owner")
    memberships = relationship("ResearchMember", back_populates="user")
    assigned_tasks = relationship("ResearchTask", back_populates="assignee")