from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, TEXT
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime, timezone


class ResearchTask(Base):
    __tablename__ = "research_tasks"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("research_projects.id"), nullable=False)
    title = Column(VARCHAR(155), nullable=False)
    description = Column(TEXT, nullable=True)
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(VARCHAR(100), nullable=False)
    priority = Column(VARCHAR(100), nullable=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    project = relationship("ResearchProject", back_populates="tasks")
    assignee = relationship("User", back_populates="assigned_tasks")