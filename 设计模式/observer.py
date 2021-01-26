# -*- coding: utf-8 -*-

class Subject(object):

    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class Observer(object):

    def __init__(self, subject, str_name):
        self.subject = subject
        self.str_name = str_name
    
    def update(self):
        pass


class StockObserver(Observer):

    def update(self):
        print "%s, stop watching Stock and go on work!" % self.str_name


class NBAObserver(Observer):

    def update(self):
        print "%s, stop watching NBA and got on work" % self.str_name


if __name__ == '__main__':
    sub = Subject()
    p1 = StockObserver(sub, 'xiaoli')
    p2 = NBAObserver(sub, 'xiaozhang')

    sub.attach(p1)
    sub.attach(p2)

    sub.notify()