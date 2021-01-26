# -*- coding: utf-8 -*-

class Player(object):
    
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defense(self):
        pass


class Forwards(Player):

    def attack(self):
        print '前锋%s，进攻' % self.name

    def defense(self):
        print '前锋%s, 防守' % self.name


class Center(Player):

    def attack(self):
        print '中锋%s，进攻' % self.name
    
    def defense(self):
        print '中锋%s，防守' % self.name


class Guards(Player):

    def attack(self):
        print '后卫%s, 进攻' % self.name

    def defense(self):
        print '后卫%s，防守' % self.name


class ForeignCenter(object):

    def __init__(self, name):
        self.name = name
    
    def ack(self):
        print '外籍中锋%s，进攻' % self.name

    def defen(self):
        print '外籍中锋%s，防守' % self.name


class Translator(Player):

    def __init__(self, name):
        self.foreignCenter = ForeignCenter(name)
    
    def attack(self):
        self.foreignCenter.ack()

    def defense(self):
        self.foreignCenter.defen()

    
if __name__ == "__main__":
    
    b = Forwards('巴蒂尔')
    m = Guards('麦克格雷迪')
    ym = Translator('姚明')

    b.attack()
    m.attack()
    ym.attack()
    ym.defense()