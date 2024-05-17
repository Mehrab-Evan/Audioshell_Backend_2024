# Book list table
from sqlalchemy import Column, Integer, String
from database import Base

class BookList(Base):
    __tablename__ = 'book_list'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)
    genre = Column(String)
    user_id = Column(Integer)