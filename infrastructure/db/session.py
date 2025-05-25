from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from infrastructure.db.models import Base

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
