# -*- coding: utf-8 -*-
class AbstractClass(object):
    
    def TemplateMethod(self):
        self.PrimitiveOperation1()
        self.PrimitiveOperation2()

    def PrimitiveOperation1(self):
        pass

    def PrimitiveOperation2(self):
        pass


class ConcreteClassA(AbstractClass):

    def PrimitiveOperation1(self):
        print 'A operation 1'

    def PrimitiveOperation2(self):
        print 'A operation 2'


class ConcreteClassB(AbstractClass):

    def PrimitiveOperation1(self):
        print 'B operation 1'

    def PrimitiveOperation2(self):
        print 'B operation 2'


if __name__ == "__main__":
    C1 = ConcreteClassA()
    C2 = ConcreteClassB()

    C1.TemplateMethod()
    C2.TemplateMethod()