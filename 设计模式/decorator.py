# -*- coding: utf-8 -*-
# 装饰模式
class Person(object):

    def __init__(self, tname):
        self.name = tname
    
    def show(self):
        print 'dress is %s' % (self.name)


class Finery(Person):
    
    compent = None

    def __init__(self):
        pass

    def decorate(self, ct):
        self.compent = ct
    
    def show(self):
        if self.compent != None:
            self.compent.show()


class Tshirts(Finery):

    def __init__(self):
        pass

    def show(self):
        print 'Big T-shirts'
        self.compent.show()


class BigTrouser(Finery):

    def __init__(self):
        pass

    def show(self):
        print 'Big Trouser'
        self.compent.show()


if __name__ == "__main__":
    p = Person("somebody")
    bt = BigTrouser()
    ts = Tshirts()
    bt.decorate(p)
    ts.decorate(bt)
    ts.show()
    