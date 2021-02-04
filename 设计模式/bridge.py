# -*- coding: utf-8 -*-
# 桥接模式
class HandsetSoft(object):
    def run(self):
        pass


class HandsetGame(HandsetSoft):

    def run(self):
        print '运行手机游戏'


class HandsetAddressList(HandsetSoft):

    def run(self):
        print '运行手机通讯录'


class HandsetBrand(object):

    def __init__(self):
        self.soft = None
    
    def setHandsetSoft(self, temp):
        self.soft = temp
    
    def run(self):
        pass


class HandsetBrandN(HandsetBrand):

    def run(self):
        print 'handsetBrand N ',
        if self.soft != None:
            self.soft.run()


class HandsetBrandM(HandsetBrand):

    def run(self):
        print 'handsetBrand M ',
        if self.soft != None:
            self.soft.run()


if __name__ == '__main__':
    ab = HandsetBrandN()
    ab.setHandsetSoft(HandsetAddressList())
    ab.run()

    ab = HandsetBrandM()
    ab.setHandsetSoft(HandsetGame())
    ab.run()