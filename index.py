from sqlalchemy.orm import sessionmaker
from news import Base
from pars import Parser
from connect import engine

parser = Parser()
news = parser.parse()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()


session.add_all(news)
session.commit()
session.close()
