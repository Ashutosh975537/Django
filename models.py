from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class RequestLog(Base):
    __tablename__ = "request_logs"  # This will be the table name in logs.db

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    request_id = Column(String, index=True)
    response_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)  # Auto-filled when the log is created
