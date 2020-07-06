from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://gordondalos:212354568789@localhost/eco_info", encoding='utf-8', echo=True)
path_ffin = 'https://ffin.ru/market/news/'