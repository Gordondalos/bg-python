from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(255))
    link_news = Column(String(255))
    date_create = Column(String(255))
    description = Column(Text)
    external_id = Column(String(55))

    def __init__(self, title, link_news, date_create, description, external_id):
        self.title = title
        self.link_news = link_news
        self.date_create = date_create
        self.description = description
        self.external_id = external_id