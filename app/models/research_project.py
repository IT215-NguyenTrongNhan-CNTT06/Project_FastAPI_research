from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, TEXT
from app.db.database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class ResearchProject(Base):
    __tablename__ = "research_projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(TEXT, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    owner = relationship("User", back_populates="owned_projects")
    members = relationship("ResearchMember", back_populates="project", cascade="all, delete-orphan")
    tasks = relationship("ResearchTask", back_populates="project", cascade="all, delete-orphan")


class ResearchMember(Base):
    __tablename__ = "research_members"

    project_id = Column(Integer, ForeignKey("research_projects.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    role = Column(VARCHAR(100), nullable=False)
    joined_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    project = relationship("ResearchProject", back_populates="members")
    user = relationship("User", back_populates="memberships")