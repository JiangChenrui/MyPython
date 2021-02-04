# -*- coding: utf-8 -*-
# 代理模式
class GiveGift(object):

    def GiveDolls():
        pass

    def GiveFlowers():
        pass

    def GiveChocolate():
        pass


class SchoolGirl(object):

    name = None

    def __init__(self):
        pass


class Pursuit(GiveGift):

    mm = None

    def __init__(self, mm):
        self.mm = mm
    
    def GiveDolls(self):
        print self.mm.name + '送你洋娃娃'
    
    def GiveFlowers(self):
        print self.mm.name + '送你鲜花'

    def GiveChocolate(self):
        print self.mm.name + '送你巧克力'


class Proxy(GiveGift):

    gg = None

    def __init__(self, mm):
        self.gg = Pursuit(mm)
    
    def GiveDolls(self):
        self.gg.GiveDolls()

    def GiveFlowers(self):
        self.gg.GiveFlowers()
    
    def GiveChocolate(self):
        self.gg.GiveChocolate()


if __name__ == "__main__":
    jiaojiao = SchoolGirl()
    jiaojiao.name = "李娇娇"

    daili = Proxy(jiaojiao)

    daili.GiveDolls()
    daili.GiveFlowers()
    daili.GiveChocolate()