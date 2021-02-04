# -*- coding: utf-8 -*-
# 组合模式
class Component:

    def __init__(self,strName):
        self.name = strName

    def Add(self, com):
        pass

    def Remove(self, com):
        pass

    def Display(self, depth):
        pass


class Leaf(Component):

    def Add(self, com):
        print "leaf can't add"

    def Remove(self, com):
        print "leaf can't remove"

    def Display(self, depth):
        print '-' * depth + self.name
    

class Composite(Component):

    def __init__(self, strName):
        self.name = strName
        self.c = []

    def Add(self, com):
        self.c.append(com)

    def Display(self, depth):
        print '-' * depth + self.name
        for com in self.c:
            com.Display(depth+2)


if __name__ == "__main__":
    p = Composite("Wong")
    p.Add(Leaf("Lee"))
    p.Add(Leaf("Zhao"))
    p1 = Composite("Wu")
    p1.Add(Leaf("San"))
    p.Add(p1)
    p.Display(1)