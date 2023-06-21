# -*- coding: utf-8  -*-
from contextlib import contextmanager
import json
import random
import time
from sqlalchemy import Column, Index, UniqueConstraint, Integer, String, create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE = declarative_base()

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


class CompensationList(BASE):

    __tablename__ = "compensation_list"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, default=0)
    notice_id = Column(Integer, default=0)
    
    __table_args__ = (
        UniqueConstraint(user_id, notice_id, name='compensation_unique'),
    )

    def __repr__(self):
        ret = {
            'id': self.id,
            'user_id': self.user_id,
            'notice_id': self.notice_id
        }
        return json.dumps(ret)


engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test', echo=False)
BASE.metadata.create_all(engine)

DBsession = sessionmaker(bind=engine)


class UserInfoExtra(BASE):

    __tablename__ = "user_info_extra"
    id = Column(Integer, primary_key=True)
    theme_free_and_bonus_data = Column(String(2048), name='yy8')

    theme_free_and_bonus = None

    def initialize(self):
        if self.theme_free_and_bonus_data is None:
            self.theme_free_and_bonus_data = json.dumps({})
        self.theme_free_and_bonus = json.loads(self.theme_free_and_bonus_data)
        if not self.theme_free_and_bonus:
            self.theme_free_and_bonus['free_tid_list'] = []
            self.theme_free_and_bonus['free_spin_list'] = []
            self.theme_free_and_bonus['bonus_tid_list'] = []
    
    def get_theme_free_and_bonus(self):
        return {
            'free_game_dict': dict(zip(self.theme_free_and_bonus['free_tid_list'], self.theme_free_and_bonus['free_spin_list'])),
            'bonus_game_list': self.theme_free_and_bonus['bonus_tid_list']
        }

    def add_theme_free(self, tid, free_spins):
        if tid not in self.theme_free_and_bonus['free_tid_list'] and free_spins > 0:
            self.theme_free_and_bonus['free_tid_list'].append(tid)
            self.theme_free_and_bonus['free_spin_list'].append(free_spins)
            if len(self.theme_free_and_bonus['free_tid_list']) > 50:
                self.theme_free_and_bonus['free_tid_list'].pop(0)
                self.theme_free_and_bonus['free_spin_list'].pop(0)
    
    def remove_theme_free(self, tid):
        if tid in self.theme_free_and_bonus['free_tid_list']:
            idx = self.theme_free_and_bonus['free_tid_list'].index()
            self.theme_free_and_bonus['free_tid_list'].pop(idx)
            self.theme_free_and_bonus['free_spin_list'].pop(idx)
    
    def add_theme_bonus(self, tid):
        if tid not in self.theme_free_and_bonus['bonus_tid_list']:
            self.theme_free_and_bonus['bonus_tid_list'].append(tid)
            if len(self.theme_free_and_bonus['bonus_tid_list']) > 50:
                self.theme_free_and_bonus['bonus_tid_list'].pop(0)
    
    def remove_theme_bonus(self, tid):
        if tid in self.theme_free_and_bonus['bonus_tid_list']:
            self.theme_free_and_bonus['bonus_tid_list'].remove(tid)
    
    def save(self):
        with get_db_session() as db_session:
            self.theme_free_and_bonus_data = json.dumps(self.theme_free_and_bonus)
            db_session.merge(self)


# start_ts = time.time()
with get_db_session() as db_session:
    for notice_id in range(3):
        for i in range(1000):
            compensation_list = CompensationList()
            compensation_list.user_id = i
            compensation_list.notice_id = notice_id
            db_session.add(compensation_list)
# end_ts = time.time()
# print(end_ts-start_ts)


# with get_db_session() as db_session:
#     result = db_session.query(SystemNotice).filter_by(id=1).first()
#     result.title = 'test'
#     result.prize_info = '{"cash": 2}'
#     db_session.merge(result)


    
