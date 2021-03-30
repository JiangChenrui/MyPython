# -*- coding: utf-8 -*-
class Product(object):
    
    def __init__(self):
        self.parts = []

    def Add(self, part):
        self.parts.append(part)

    def Show(self):
        for part in self.parts:
            print part,
        print

class Builder(object):

    def __init__(self):
        self.product = Product()

    def BuildPartA(self):
        pass

    def BuildPartB(self):
        pass

    def GetResult(self):
        pass


class ConcreteBuilder1(Builder):

    def BuildPartA(self):
        self.product.Add('部件A')
    
    def BuildPartB(self):
        self.product.Add('部件B')

    def GetResult(self):
        return self.product


class ConcreteBuilder2(Builder):

    def BuildPartA(self):
        self.product.Add('部件X')
    
    def BuildPartB(self):
        self.product.Add('部件Y')

    def GetResult(self):
        return self.product


class Director(object):

    def ConSruct(self, builder):
        builder.BuildPartA()
        builder.BuildPartB()


if __name__ == '__main__':
    director = Director()
    b1 = ConcreteBuilder1()
    b2 = ConcreteBuilder2()

    director.ConSruct(b1)
    p1 = b1.GetResult()
    p1.Show()

    director.ConSruct(b2)
    p2 = b2.GetResult()
    p2.Show()
