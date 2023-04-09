from sqlalchemy import Column, Integer, String
from config import Base


class Book(Base):
    _tablename_ = 'Books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publishedyear = Column(Integer)
    
