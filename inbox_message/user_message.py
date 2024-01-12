# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, and_
from mysql_config import Base, get_db_session, DB, db_init


class UserMessage(Base):

    __tablename__ = 'user_message'

    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer, index=True)

    
def get_user_message():
    with get_db_session() as db_session:
        user_message_item = db_session.query(UserMessage).filter(and_(
            UserMessage.user_id == 16789,
        )).first()
        if user_message_item is None:
            user_message_item = UserMessage(user_id=16789)
            db_session.add(user_message_item)
            db_session.flush()
        db_session.expunge(user_message_item)
    return user_message_item

def run():
    db_init()
    user_message = get_user_message()
    print(user_message.user_id)

run()

