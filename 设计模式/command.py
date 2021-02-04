# -*- coding: utf-8 -*-
# 命令模式
class Barbucer(object):

    def MakeMutton(self):
        print "Mutton"

    def MakeChickenWing(self):
        print "Chicken Wing"

class Command(object):

    def __init__(self, receiver):
        self.receiver = receiver

    def excuteCommand(self):
        pass


class BakeMuttonCommand(Command):

    def excuteCommand(self):
        self.receiver.MakeMutton()


class BakeChickenWingCommand(Command):

    def excuteCommand(self):
        self.receiver.MakeChickenWing()


class Waiter(object):

    def __init__(self):
        self.order = []

    def SetOrder(self, command):
        self.order.append(command)
    
    def Notify(self):
        for cmd in self.order:
            cmd.excuteCommand()


if __name__ == "__main__":
    barbucer=Barbucer()
    cmd = BakeChickenWingCommand(barbucer)
    cmd2 = BakeMuttonCommand(barbucer)
    girl = Waiter()
    girl.SetOrder(cmd)
    girl.SetOrder(cmd2)
    girl.Notify()

