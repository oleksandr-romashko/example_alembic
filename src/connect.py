import os

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

os.makedirs("data", exist_ok=True)

url_to_db = "sqlite:///data/mynotes.db"
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
session = Session()
