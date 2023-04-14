# -*- coding: utf-8  -*-
from contextlib import contextmanager
import json
from sqlalchemy import Column, Integer, String, create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE = declarative_base()

class SystemNotice(BASE):

    __tablename__ = "system_notice"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    title = Column(String(64), default='')
    prize_info = Column(String(64), default='')

    def __repr__(self):
        ret = {
            'id': self.id,
            'title': self.title,
            'prize_info': self.prize_info
        }
        return json.dumps(ret)


engine = create_engine('mysql+pymysql://root@localhost:3306/test', echo=False)
BASE.metadata.create_all(engine)

DBsession = sessionmaker(bind=engine)

@contextmanager
def get_db_session():
    session = DBsession()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise
    finally:
        session.close()

# for i in range(10):
#     with get_db_session() as db_session:
#         new_system_notice = SystemNotice()
#         new_system_notice.user_id = 16789
#         new_system_notice.title = 'test'
#         new_system_notice.prize_info = '{"cash": 1}'
#         db_session.add(new_system_notice)


# with get_db_session() as db_session:
#     result = db_session.query(SystemNotice).filter_by(id=1).first()
#     result.title = 'test'
#     result.prize_info = '{"cash": 2}'
#     db_session.merge(result)

with get_db_session() as db_session:
    query_list = [SystemNotice.user_id == str(16789)]
    sys_notice = db_session.query(SystemNotice.id).filter(*query_list).order_by(SystemNotice.id.desc()).limit(20).all()
    print(sys_notice)
    
