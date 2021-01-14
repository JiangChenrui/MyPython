# -*- coding: utf-8 -*-

class Operation(object):

    def getResult(self):
        pass
    

class OperationAdd(Operation):

    def getResult(self):
        return self.op1 + self.op2


class OperationSub(Operation):

    def getResult(self):
        return self.op1 - self.op2


class OperationMul(Operation):

    def getResult(self):
        return self.op1 * self.op2


class OperationDiv(Operation):

    def getResult(self):
        try:
            result = self.op1 / self.op2
            return result
        except:
            print "error:divided by zero."
            return 0


class OperationUef(Operation):

    def getResult(self):
        print "Undefine operation."
        return 0


class OperationFactory(object):

    operation = {}
    operation['+'] = OperationAdd()
    operation['-'] = OperationSub()
    operation['*'] = OperationMul()
    operation['/'] = OperationDiv()

    def createOperation(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUef()
        return op


if __name__ == "__main__":
    op = '+'
    opa = 10
    opb = 5
    factory = OperationFactory()
    cal = factory.createOperation(op)
    cal.op1 = opa
    cal.op2 = opb
    print cal.getResult()