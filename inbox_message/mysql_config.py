# -*- coding: utf-8 -*-
import random
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOST = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'mysqltest'
DB_NAME = 'myclass'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s'%(USERNAME,PASSWORD,HOST,PORT,DB_NAME)

DB = {}
Base = declarative_base()

def db_init():
    engine = create_engine(DB_URI)
    Base.metadata.create_all(engine)
    DB['0'] = sessionmaker(bind=engine, autoflush=False, expire_on_commit=True)


@contextmanager
def get_db_session():
    session = DB['0']()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
