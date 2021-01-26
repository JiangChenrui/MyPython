# -*- coding: utf-8 -*-

class Originator(object):

    def __init__(self):
        self.state = ''
    
    def createMemento(self):
        return Memento(self.state)

    def setMemeto(self, memento):
        self.state = memento.state
    
    def show(self):
        print 'State = %s' % self.state 


class Memento(object):

    def __init__(self, state):
        self.state = state
    

class Caretaker(object):

    def __init__(self):
        self.memento = None


if __name__ == "__main__":
    o = Originator()
    o.state = 'On'
    o.show()

    c = Caretaker()
    c.memento = o.createMemento()

    o.state = 'Off'
    o.show()
    
    o.setMemeto(c.memento)
    o.show()