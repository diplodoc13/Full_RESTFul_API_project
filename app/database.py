
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:parol123@localhost:5432/fastapi_course'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

"""
It creates a database connection, and then yields it to the caller. 
The caller can then use the connection, and when it's done, the connection is closed. 
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()