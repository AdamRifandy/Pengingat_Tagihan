import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

engine = create_engine(f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}", echo=True)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine)