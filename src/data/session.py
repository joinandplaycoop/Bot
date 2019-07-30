import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import Config

engine = create_engine(Config.cfg.mysql.connectionString)
Session = sessionmaker(bind=engine)