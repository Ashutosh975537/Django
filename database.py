from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite DB file path — will be created in current folder
DATABASE_URL = "sqlite:///./logs.db"

# Create a database engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session factory (used in dependencies)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for all your models to inherit from
Base = declarative_base()
