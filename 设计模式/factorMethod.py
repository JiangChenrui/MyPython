# -*- coding: utf-8 -*-
# 工厂方法模式
class Leifeng(object):

    def Sweep(self):
        print "Lefifen Sweep"


class Student(Leifeng):

    def Sweep(self):
        print "Student Sweep"


class Volenter(Leifeng):

    def Sweep(self):
        print "Volenter Sweep"


class LeifenFactory(object):

    def createLeifeng(self):
        return Leifeng()


class StudentFactory(LeifenFactory):

    def createLeifeng(self):
        return Student()


class VolenterFactory(LeifenFactory):

    def createLeifeng(self):
        return Volenter()


if __name__ == "__main__":
    sf = StudentFactory()
    s = sf.createLeifeng()
    s.Sweep()
    sdf = VolenterFactory()
    sd = sdf.createLeifeng()
    sd.Sweep()