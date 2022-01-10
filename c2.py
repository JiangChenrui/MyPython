# -*- coding: utf-8 -*-
import json
import copy
from sqlalchemy import Column, Integer, String, Float, and_

from models.initialize import BASE, get_db_session


class FrenzyCash(BASE):
    """代金账户"""
    __tablename__ = "frenzy_cash"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)

    frenzy_cash_num = Column(Float, default=0.0)

    alter_num1 = Column(Integer, default=0)
    alter_num2 = Column(Integer, default=0)
    alter_num3 = Column(Integer, default=0)
    alter_num4 = Column(Integer, default=0)

    alter_data1 = Column(String(1024), default='[]')
    alter_data2 = Column(String(1024), default='[]')
    alter_data3 = Column(String(4096), default='[]')
    alter_data4 = Column(String(4096), default='[]')

    def initialize(self, ctx, pkg):
        self._ctx = ctx

    def get_status(self):
        ret = {
            u'frenzy_cash': self.frenzy_cash_num
        }
        return ret

    def get_frenzy_cash(self):
        return self.frenzy_cash_num

    def add_frenzy_cash(self, delta_num, place):
        """增加游戏币数量"""
        self.frenzy_cash_num = round(self.frenzy_cash_num + delta_num, 2)
        log = [
            ['cmd', 0],
            ['add', delta_num],
            ['fc', self.frenzy_cash_num],
            ['from', place]
        ]
        self._log(extra_log=log)

    def consume_frenzy_cash(self, consume_num, place='N/a'):
        """消耗游戏币"""
        ret = False
        if self.frenzy_cash_num >= consume_num:
            self.frenzy_cash_num = round(self.frenzy_cash_num - consume_num, 2)
            log = [
                ['cmd', 1],
                ['c_num', consume_num],
                ['fc', self.frenzy_cash_num],
                ['place', place]
            ]
            ret = True
            self._log(extra_log=log)
        return ret

    def save_frenzy_cash(self, pkg):
        with get_db_session(pkg) as db_session:
            db_session.merge(self)
            info('save frenzy cash user_id=%d' % self.user_id)

    def get_value(self, key):
        if len(key) < 30:
            value = eval('self.' + key)
            return json.dumps(value)

    def set_value(self, pkg, key, value):
        if len(key) < 30:
            exec 'self.' + key + '=' + value
            self.save_frenzy_cash(pkg)
            return value

    def _log(self, extra_log=None, less_log=False):
        """Logs some basic info of user and extra info about every segment of the game."""
        from log import log_slot_game

        if extra_log is None:
            extra_log = []
        if less_log:
            log = [
                ['id', self._ctx.user.id],
            ]
        else:
            log = [
                ['id', self._ctx.user.id],
                ['lv', self._ctx.user.level],
                ['vip', self._ctx.user.vip_level],
                ['rlv', self._ctx.property.r_level],
                ['pkgid', self._ctx.pkg_id],
                ['pt', self._ctx.user.total_purchase],
                ['ip', self._ctx.ip_address],
                ['hlo', self._ctx.user_persona.purchase_type]
            ]

        if extra_log:
            log.extend(extra_log)

        log_slot_game('frenzy_cash', log)


def get_frenzy_cash(ctx, pkg, user_id):
    with get_db_session(pkg) as db_session:
        frenzy_cash_item = db_session.query(FrenzyCash).filter(and_(
            FrenzyCash.user_id == user_id,
        )).first()
        if frenzy_cash_item is None:
            frenzy_cash_item = FrenzyCash(user_id=user_id)
            db_session.add(frenzy_cash_item)
            db_session.flush()
        db_session.expunge(frenzy_cash_item)
        frenzy_cash_item.initialize(ctx, pkg)
    return frenzy_cash_item

