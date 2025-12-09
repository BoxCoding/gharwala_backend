from sqlalchemy import create_engine, Column,String,Float,Datetime,JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from datetime import datetime
from config.settings import settings
from utils.logger import logger

#SQLAlchemy setup
Base=declarative_base()
engine=create_engine(settings.postgres_database_url)
SessionLocal=sessionmaker(bind=engine)

#MongoDB setup
mongo_client=MongoClient(settings.MONGODB_URL)
mongodb=mongo_client[settings.MONGODB_NAME]