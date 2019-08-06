import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import Config
from datetime import datetime as d

engine = create_engine(Config.cfg.mysql.connectionString)
Session = sessionmaker(bind=engine)
connectionStartTime = d.now()

def connect():
    global engine
    global Session
    global connectionStartTime
    engine = create_engine(Config.cfg.mysql.connectionString)
    Session = sessionmaker(bind=engine)
    connectionStartTime = d.now()

connect()