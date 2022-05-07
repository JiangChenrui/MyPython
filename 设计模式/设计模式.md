# 设计模式

* 单一职责(SRP)
* 开闭原则(OCP)
* 依赖倒转(ASD)
* 里氏代换(LSP)
* 合成聚合复用
* 迪米特法则
    如果两个类不必彼此直接通信，那么这两个类就不应当发生直接的相互作用，如果其中一个类需要调用另一个类的某一个方法的话，可以通过第三者转发这个调用

**内聚性描述的是一个例程内部组成部分之间相互联系的紧密程度。而耦合性描述的是一个例程与其他例程之间联系的紧密程度。软件开发的目标应该是创建这样的例程：内部完整，也就是高内聚，而与其他例程之间的联系则是小巧、直接、可见、灵活的，这就是松耦合[DPE]**

## 简单工厂模式

* 可维护
* 可复用
* 可扩展
* 灵活性好

通过封装、继承、多态把程序的耦合度降低

```python
# -*- coding: utf-8 -*-
# 简单工厂模式
class Operation(object):
    op1 = 0
    op2 = 0

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
```

## 策略模式

面向对象的编程，并不是类越多越好，类的划分是为了封装，但分类的基础是抽象，具有相同属性和功能的对象的抽象集合才是类。

策略模式定义了算法家族，分别封装起来，让他们之间可以互相替换，此模式让算法的变化，不会影响到使用算法的客户。

```python
# -*- coding: utf-8 -*-
# 策略模式

class CashSuper(object):

    def acceptCash(self):
        return 0


class CashNormal(CashSuper):

    def acceptCash(self, money):
        return money


class CashRebate(CashSuper):

    discount = 1

    def __init__(self, discount):
        self.discount = discount

    def acceptCash(self, money):
        return self.discount * money


class CashReturn(CashSuper):

    total = 0

    ret = 0

    def __init__(self, total, ret):
        self.total = total
        self.ret = ret
    
    def acceptCash(self, money):
        if money >= self.total:
            return money - self.ret
        else:
            return money


class CashContext(object):

    def __init__(self, cashSuper):
        self.cs = cashSuper

    def getResult(self, money):
        return self.cs.acceptCash(money)


if __name__ == "__main__":
    money = input("money:")
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300,100))
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for 300 -100.")
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print "Undefine type.Use normal mode."
        cc = strategy[1]
    print "you will pay:%d" %(cc.getResult(money))
```

## 装饰模式

动态地给一个对象添加一些额外的职责，就增加功能来说，装饰模式比生成子类更为灵活

```python
# -*- coding: utf-8 -*-
# 装饰模式
class Person(object):

    def __init__(self, tname):
        self.name = tname
    
    def show(self):
        print 'dress is %s' % (self.name)


class Finery(Person):
    
    compent = None

    def __init__(self):
        pass

    def decorate(self, ct):
        self.compent = ct
    
    def show(self):
        if self.compent != None:
            self.compent.show()


class Tshirts(Finery):

    def __init__(self):
        pass

    def show(self):
        print 'Big T-shirts'
        self.compent.show()


class BigTrouser(Finery):

    def __init__(self):
        pass

    def show(self):
        print 'Big Trouser'
        self.compent.show()


if __name__ == "__main__":
    p = Person("somebody")
    bt = BigTrouser()
    ts = Tshirts()
    bt.decorate(p)
    ts.decorate(bt)
    ts.show()
    
```

## 代理模式

为其他对象提供一种代理以控制对这个对象的访问

```python
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
```

## 工厂方法模式

定义一个用于创建对象的接口，让子类决定实例化哪一个类，工厂方法使一个类的实例化延迟到其子类

```python
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
```

## 原型模式

用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象

```python
# -*- coding: utf-8 -*-
# 原型模式
import copy


class WorkExp:
    place = ""
    year = 0


class Resume:

    name = ''

    age = 0

    def __init__(self,n):
        self.name = n

    def SetAge(self,a):
        self.age = a

    def SetWorkExp(self,p,y):
        self.place = p
        self.year = y

    def Display(self):
        print self.age
        print self.place
        print self.year
        
    def Clone(self):
    # 实际不是“克隆”，只是返回了自身
        return self


if __name__ == "__main__":
    a = Resume("a")
    b = a.Clone()
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a.SetAge(7)
    b.SetAge(12)
    c.SetAge(15)
    d.SetAge(18)
    a.SetWorkExp("PrimarySchool",1996)
    b.SetWorkExp("MidSchool",2001)
    c.SetWorkExp("HighSchool",2004)
    d.SetWorkExp("University",2007)
    a.Display()
    b.Display()
    c.Display()
    d.Display()
```

## 模板方法模式

定义一个操作中的算法的骨架，而将一些步骤延迟到子类中，模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

```python
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
```

## 外观模式

为子系统中的一组接口提供一个一致的界面，此模式定义了一个高层接口，这个接口使得这一子系统更加容易使用

```python
# -*- coding: utf-8 -*-
# 外观模式
class SubSystemOne:

    def MethodOne(self):
        print "SubSysOne"

class SubSystemTwo:

    def MethodTwo(self):
        print "SubSysTwo"

class SubSystemThree:

    def MethodThree(self):
        print "SubSysThree"

class SubSystemFour:

    def MethodFour(self):
        print "SubSysFour"


class Facade:

    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()

    def MethodA(self):
        print "MethodA"
        self.one.MethodOne()
        self.two.MethodTwo()
        self.four.MethodFour()
        
    def MethodB(self):
        print "MethodB"
        self.two.MethodTwo()
        self.three.MethodThree()


if __name__ == "__main__":
    facade = Facade()
    facade.MethodA()
    facade.MethodB()
```

## 建造者模式

将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示

```python
# 建造者模式

class Person:
    def CreateHead(self):
        pass
    def CreateHand(self):
        pass
    def CreateBody(self):
        pass
    def CreateFoot(self):
        pass

class ThinPerson(Person):
    def CreateHead(self):
        print "thin head"
    def CreateHand(self):
        print "thin hand"
    def CreateBody(self):
        print "thin body"
    def CreateFoot(self):
        print "thin foot"

class ThickPerson(Person):
    def CreateHead(self):
        print "thick head"
    def CreateHand(self):
        print "thick hand"
    def CreateBody(self):
        print "thick body"
    def CreateFoot(self):
        print "thick foot"

class Director:
    def __init__(self,temp):
        self.p = temp
    def Create(self):
        self.p.CreateHead()
        self.p.CreateBody()
        self.p.CreateHand()
        self.p.CreateFoot()

if __name__ == "__main__":
    p = ThickPerson()
    d = Director(p)
    d.Create()
```

## 观察者模式

观察者模式定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象，这个主题对象在状态发生变化时，会通知所有观察者对象，是它们能够自动更新自己。

```python
# -*- coding: utf-8 -*-
# 观察者模式
class Subject(object):

    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class Observer(object):

    def __init__(self, subject, str_name):
        self.subject = subject
        self.str_name = str_name
    
    def update(self):
        pass


class StockObserver(Observer):

    def update(self):
        print "%s, stop watching Stock and go on work!" % self.str_name


class NBAObserver(Observer):

    def update(self):
        print "%s, stop watching NBA and got on work" % self.str_name


if __name__ == '__main__':
    sub = Subject()
    p1 = StockObserver(sub, 'xiaoli')
    p2 = NBAObserver(sub, 'xiaozhang')

    sub.attach(p1)
    sub.attach(p2)

    sub.notify()
```

## 抽象工厂模式

提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类

```python
# -*- coding: utf-8 -*-
# 抽象工厂
class IUser:

    def GetUser(self):
        pass

    def InsertUser(self):
        pass

class IDepartment:

    def GetDepartment(self):
        pass

    def InsertDepartment(self):
        pass

class CAccessUser(IUser):

    def GetUser(self):
        print "Access GetUser"

    def InsertUser(self):
        print "Access InsertUser"


class CAccessDepartment(IDepartment):

    def GetDepartment(self):
        print "Access GetDepartment"

    def InsertDepartment(self):
        print "Access InsertDepartment"

class CSqlUser(IUser):

    def GetUser(self):
        print "Sql GetUser"

    def InsertUser(self):
        print "Sql InsertUser"


class CSqlDepartment(IDepartment):

    def GetDepartment(self):
        print "Sql GetDepartment"

    def InsertDepartment(self):
        print "Sql InsertDepartment"

class IFactory:

    def CreateUser(self):
        pass

    def CreateDepartment(self):
        pass

class AccessFactory(IFactory):

    def CreateUser(self):
        temp = CAccessUser()
        return temp

    def CreateDepartment(self):
        temp = CAccessDepartment()
        return temp

class SqlFactory(IFactory):

    def CreateUser(self):
        temp = CSqlUser()
        return temp

    def CreateDepartment(self):
        temp = CSqlDepartment()
        return temp


if __name__ == "__main__":
    factory = SqlFactory()
    user = factory.CreateUser()
    depart = factory.CreateDepartment()
    user.GetUser()
    depart.GetDepartment()
```

## 状态模式

当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类。状态模式主要解决的是当控制一个对象状态转换的条件表达式过于复杂时的情况，把状态的判断逻辑转移到不同状态的一系列类当中，可以把复杂的判断逻辑简化

```python
# -*- coding: utf-8 -*-
# 状态模式
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
```

## 适配器模式

将一个类的接口转换成客户希望的另一个接口，适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作

```python
# -*- coding: utf-8 -*-
# 适配器模式
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
```

## 备忘录模式

在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样以后就可将该对象恢复到原先保存的状态

```python
# -*- coding: utf-8 -*-
# 备忘录模式
class Originator(object):

    def __init__(self):
        self.state = ''
    
    def createMemento(self):
        return Memento(self.state)

    def setMemeto(self, memento):
        self.state = memento.state
    
    def show(self):
        print 'State = %s' % self.state 


class Memento(object):

    def __init__(self, state):
        self.state = state
    

class Caretaker(object):

    def __init__(self):
        self.memento = None


if __name__ == "__main__":
    o = Originator()
    o.state = 'On'
    o.show()

    c = Caretaker()
    c.memento = o.createMemento()

    o.state = 'Off'
    o.show()
    
    o.setMemeto(c.memento)
    o.show()
```

## 组合模式

将对象组合成树形结构以表示‘部分-整体’的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性

```python
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
```

## 单例模式

保证应该类仅有应该实例，并提供一个访问它的全局访问点

[python装饰器](https://foofish.net/python-decorator.html)

```python
# -*- encoding=utf-8 -*-
print '----------------------方法1--------------------------'
# 方法1,实现__new__方法
# 并在将一个类的实例绑定到类变量_instance上,
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._instance不为None,直接返回cls._instance

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()

two.a = 3
print one.a
# 3
# one和two完全相同,可以用id(), ==, is检测
print id(one)
# 29097904
print id(two)
# 29097904
print one == two
# True
print one is two
# True

print '----------------------方法2--------------------------'
# 方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)
# 同一个类的所有实例天然拥有相同的行为(方法),
# 只需要保证同一个类的所有实例具有相同的状态(属性)即可
# 所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)
# 可参看:http://code.activestate.com/recipes/66531/
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1

one = MyClass2()
two = MyClass2()

# one和two是两个不同的对象,id, ==, is对比结果可看出
two.a = 3
print one.a
# 3
print id(one)
# 28873680
print id(two)
# 28873712
print one == two
# False
print one is two
# False
# 但是one和two具有相同的（同一个__dict__属性）,见:
print id(one.__dict__)
# 30104000
print id(two.__dict__)
# 30104000

print '----------------------方法3--------------------------'
# 方法3:本质上是方法1的升级（或者说高级）版
# 使用__metaclass__（元类）的高级python用法
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance

class MyClass3(object):
    __metaclass__ = Singleton2

one = MyClass3()
two = MyClass3()

two.a = 3
print one.a
# 3
print id(one)
# 31495472
print id(two)
# 31495472
print one == two
# True
print one is two
# True

print '----------------------方法4--------------------------'
# 方法4:也是方法1的升级（高级）版本,
# 使用装饰器(decorator),
# 这是一种更pythonic,更elegant的方法,
# 单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的
def singleton(cls):
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

one = MyClass4(x=10)
two = MyClass4(x=1)

two.a = 3
print one.a
# 3
print id(one)
# 29660784
print id(two)
# 29660784
print one == two
# True
print one is two
# True
one.x = 1
print one.x
# 1
print two.x
# 1
```

## 桥接模式

将抽象部分与它的实现部分分离，是它们都可以独立地变化。

**对象的继承关系是在编译时就定义好了，所以无法在运行是改变从父类继承的实现。子类的实现和它的父类有非常紧密的依赖关系，以至于父类中的任何变化必然会导致子类发生变化。当你需要复用子类时，如果继承下来的实现不适合解决新的问题，则父类必须重写或被其它更适合的类替换。这种依赖关系限制了灵活性并最终限制了复用性**

```python
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
```

### 合成/聚合复用原则

聚合表示一种弱的拥有关系，体现的是A对象可以包含B对象，但B对象不是A对象的一部分；合成则是一种强的拥有关系，体现了严格的部分和整体的关系，部分和整体的生命周期一样。

## 命令模式

将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化；对请求排队或者记录请求日志，以及支持可撤销的操作。

```python
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
```

## 职责链模式

使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这个对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止

```python
# -*- coding: utf-8 -*-
# 职责链模式

class Request:
    def __init__(self, tcontent, tnum):
        self.content = tcontent
        self.num = tnum


class Manager:
    def __init__(self, temp):
        self.name = temp
    def SetSuccessor(self, temp):
        self.manager = temp
    def GetRequest(self, req):
        pass


class CommonManager(Manager):
    def GetRequest(self, req):
        if(req.num>=0 and req.num<10):
            print "%s handled %d request." %(self.name, req.num)
        else:
            self.manager.GetRequest(req)


class MajorDomo(Manager):
    def GetRequest(self, req):
        if(req.num>=10):
            print "%s handled %d request." %(self.name, req.num)


if __name__ == "__main__":
    common = CommonManager("Zhang")
    major = MajorDomo("Lee")
    common.SetSuccessor(major)
    req = Request("rest", 33)
    common.GetRequest(req)
    req2 = Request("salary", 3)
    common.GetRequest(req2)
```

## 中介者模式

用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而是其耦合松散，而且可以独立地改变它们之间的交互。

```python
# -*- coding: utf-8 -*-
# 中介者模式

class Mediator:
    def Send(self, message, col):
        pass


class Colleague:
    def __init__(self, temp):
        self.mediator = temp


class Colleague1(Colleague):
    def Send(self, message):
        self.mediator.Send(message, self)
    def Notify(self, message):
        print "Colleague1 get a message: %s" % message


class Colleague2(Colleague):
    def Send(self, message):
        self.mediator.Send(message, self)
    def Notify(self, message):
        print "Colleague2 get a message: %s" % message


class ConcreteMediator(Mediator):
    def Send(self, message, col):
        if(col==col1):
            col2.Notify(message)
        else:
            col1.Notify(message)


if __name__ == "__main__":
    m = ConcreteMediator()
    col1 = Colleague1(m)
    col2 = Colleague2(m)
    m.col1 = col1
    m.col2 = col2
    col1.Send("How are you?")
    col2.Send("Fine.")
```

## 享元模式

运用共享技术有效地支持大量细粒度的对象

```python
# -*- coding: utf-8 -*-
# 享元模式

import sys

class WebSite:
    def Use(self):
        pass

class ConcreteWebSite(WebSite):
    def __init__(self, strName):
        self.name = strName
    def Use(self, user):
        print "Website type: %s, user: %s" % (self.name, user)

class UnShareWebSite(WebSite):
    def __init__(self, strName):
        self.name = strName
    def Use(self, user):
        print "UnShare Website type: %s, user: %s" % (self.name, user)

class WebFactory:
    def __init__(self):
        test = ConcreteWebSite("test")
        self.webtype ={"test": test}
        self.count = {"test": 0}
    def GetWeb(self,webtype):
        if webtype not in self.webtype:
            temp = ConcreteWebSite(webtype)
            self.webtype[webtype] = temp
            self.count[webtype] = 1
        else:
            temp = self.webtype[webtype]
            self.count[webtype] = self.count[webtype]+1
        return temp
    def GetCount(self):
        for key in self.webtype:
            #print "type: %s, count:%d" %(key,sys.getrefcount(self.webtype[key]))
            print "type: %s, count: %d " %(key,self.count[key])

if __name__ == "__main__":
    f = WebFactory()
    ws = f.GetWeb("blog")
    ws.Use("Lee")
    ws2 = f.GetWeb("show")
    ws2.Use("Jack")
    ws3 = f.GetWeb("blog")
    ws3.Use("Chen")
    ws4 = UnShareWebSite("TEST")
    ws4.Use("Mr.Q")
    print f.webtype
    f.GetCount()
```

## 解释器模式

给的一个语言，定义他的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。

如果一种特定类型的问题发生的频率足够高，那么可能就值得将该问题的各个实例表述为一个简单语言中的句子。这样就可以构建一个解释器，该解释器通过解释这些句子来解决该问题

```python
# -*- coding: utf-8 -*-
# 解释器模式

class Context:
    def __init__(self):
        self.input = ""
        self.output = ""

class AbstractExpression:
    def Interpret(self, context):
        pass

class Expression(AbstractExpression):
    def Interpret(self, context):
        print "terminal interpret"

class NonterminalExpression(AbstractExpression):
    def Interpret(self, context):
        print "Nonterminal interpret"

if __name__ == "__main__":
    context= ""
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)
```

## 访问者模式

表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变个元素的类的前提下定义作用域这些元素的新操作。

```python
# -*- coding: UTF-8 -*-
# 访问者模式

class Person:
    def Accept(self, visitor):
        pass

class Man(Person):
    def Accept(self, visitor):
        visitor.GetManConclusion(self)

class Woman(Person):
    def Accept(self, visitor):
        visitor.GetWomanConclusion(self)

class Action:
    def GetManConclusion(self, concreteElementA):
        pass
    def GetWomanConclusion(self, concreteElementB):
        pass

class Success(Action):
    def GetManConclusion(self, concreteElementA):
        print "男人成功时，背后有个伟大的女人"
    def GetWomanConclusion(self, concreteElementB):
        print "女人成功时，背后有个不成功的男人"

class Failure(Action):
    def GetManConclusion(self, concreteElementA):
        print "男人失败时，闷头喝酒，谁也不用劝"
    def GetWomanConclusion(self, concreteElementB):
        print "女人失败时，眼泪汪汪，谁也劝不了"


class ObjectStructure:
    def __init__(self):
        self.plist = []
    def Add(self, p):
        self.plist = self.plist + [p]
    def Display(self, act):
        for p in self.plist:
            p.Accept(act)

if __name__ == "__main__":
    os = ObjectStructure()
    os.Add(Man())
    os.Add(Woman())
    sc = Success()
    os.Display(sc)
    fl = Failure()
    os.Display(fl)
```