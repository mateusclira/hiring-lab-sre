from dataclasses import dataclass
from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

@dataclass
class Post(Base):
    __tablename__ = 'posts'

    id: int
    description: str
    created_by: str
    created_at: datetime

    id = Column(Integer, primary_key=True)
    description = Column(String)
    created_by = Column(String)
    created_at = Column(DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "created_by": self.created_by,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
