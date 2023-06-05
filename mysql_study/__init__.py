# -*- coding: utf-8  -*-
from contextlib import contextmanager
import json
import time
from sqlalchemy import Column, Index, UniqueConstraint, Integer, String, create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE = declarative_base()

class CompensationList(BASE):

    __tablename__ = "compenstation_list"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, default=0)
    notice_id = Column(Integer, default=0)
    prize_info = Column(String(1024), default='')

    def __repr__(self):
        ret = {
            'id': self.id,
            'user_id': self.user_id,
            'notice_id': self.notice_id,
            'prize_info': self.prize_info
        }
        return json.dumps(ret)


engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test', echo=False)
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

# start_ts = time.time()
# with get_db_session() as db_session:
#     for notice_id in range(3):
#         for i in range(1000):
#             compensation_list = CompensationList()
#             compensation_list.user_id = i
#             compensation_list.notice_id = notice_id
#             compensation_list.prize_info = '{"chips": 1}'
#             db_session.add(compensation_list)
# end_ts = time.time()
# print(end_ts-start_ts)


# with get_db_session() as db_session:
#     result = db_session.query(SystemNotice).filter_by(id=1).first()
#     result.title = 'test'
#     result.prize_info = '{"cash": 2}'
#     db_session.merge(result)

ret = {}
with get_db_session() as db_session:
    compensation_list = db_session.query(CompensationList).filter_by(notice_id=1).all()
    for i in compensation_list:
        ret[i.user_id] = json.loads(i.prize_info)
print(ret)
    
