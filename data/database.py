from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "mysql+pymysql://root:KaikeRenan11@localhost:3306/myapi"

engine = create_engine(database_url)

SessionLocal = sessionmaker (autoflush=False, autocommit = False, bind=engine)