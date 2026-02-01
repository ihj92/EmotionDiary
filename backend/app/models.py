from sqlalchemy import Column, Integer, Text, String, DateTime
from datetime import datetime
from .database import Base

class Diary(Base):
    __tablename__ = "diaries"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    emotion = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now)