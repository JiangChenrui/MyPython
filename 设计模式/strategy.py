# -*- coding: utf-8 -*-

class CashSuper(object):

    def acceptCash(self):
        return 0


class CashNormal(CashSuper):

    def acceptCash(self, money):
        return money



class CashRebate(CashSuper):

    discount = 1

    def __init__(self, discount):
        self.discount = discount

    def acceptCash(self, money):
        return self.discount * money


class CashReturn(CashSuper):

    total = 0

    ret = 0

    def __init__(self, total, ret):
        self.total = total
        self.ret = ret
    
    def acceptCash(self, money):
        if money >= self.total:
            return money - self.ret
        else:
            return money


class CashContext(object):

    def __init__(self, cashSuper):
        self.cs = cashSuper

    def getResult(self, money):
        return self.cs.acceptCash(money)


if __name__ == "__main__":
    money = input("money:")
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300,100))
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for 300 -100.")
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print "Undefine type.Use normal mode."
        cc = strategy[1]
    print "you will pay:%d" %(cc.getResult(money))