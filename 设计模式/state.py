# -*- coding: utf-8 -*-


class State(object):

    def writeProgram(self, work):
        pass


class ForenoonState(State):

    def writeProgram(self, work):
        if work.hour < 12:
            print "当前时间：%d点，上午工作" % work.hour
        else:
            work.setState(NoonState())
            work.writeProgram()


class NoonState(State):

    def writeProgram(self, work):
        if work.hour < 13:
            print "当前时间：%d点，午饭" % work.hour
        else:
            work.setState(AfternoonState())
            work.writeProgram()


class AfternoonState(State):

    def writeProgram(self, work):
        if work.hour < 17:
            print "当前时间: %d点，下午工作" % work.hour
        else:
            work.setState(EveningState())
            work.writeProgram()


class EveningState(State):
    
    def writeProgram(self, work):
        if work.finish:
            work.setState(RestState())
            work.writeProgram()
        else:
            if work.hour < 21:
                print "当前时间：%d点，社畜加班" % work.hour
            else:
                work.setState(SleepState())
                work.writeProgram()


class SleepState(State):

    def writeProgram(self, work):
        print "当前时间：%d点，终于能睡了" % work.hour


class RestState(State):

    def writeProgram(self, work):
        print "当前时间：%d点，下班回家" % work.hour


class Work(object):

    def __init__(self):
        self.current = ForenoonState()
        self.hour = 9
        self.finish = False

    def setState(self, temp):
        self.current = temp
    
    def writeProgram(self):
        self.current.writeProgram(self)


if __name__ == "__main__":
    emergencyProjects = Work()
    emergencyProjects.hour = 9
    emergencyProjects.writeProgram()
    emergencyProjects.hour = 10
    emergencyProjects.writeProgram()
    emergencyProjects.hour = 12
    emergencyProjects.writeProgram()
    emergencyProjects.hour = 13
    emergencyProjects.writeProgram()
    emergencyProjects.hour = 14
    emergencyProjects.writeProgram()
    emergencyProjects.hour = 17

    emergencyProjects.finish = False

    emergencyProjects.writeProgram()
    emergencyProjects.hour = 19
    emergencyProjects.writeProgram()
    emergencyProjects.hour = 22
    emergencyProjects.writeProgram()

