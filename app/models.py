from sqlalchemy import Column, Integer, String, Date 
from database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=False)
    description = Column(String(50), nullable=True)
    create_date = Column(Date, nullable=True)   # Date : 날짜만 저장 (연, 월, 일), DateTime : 날짜와 시간 모두 저장
    