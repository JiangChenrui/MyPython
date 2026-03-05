#-*-coding:utf-8-*-
import sys
import os
import glob
import time
import math
import re
from random import randint
from datetime import date
from functools import reduce


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return int(s) - int('0')
    return reduce(fn, map(char2num, s))


def is_odd(n):
    return n % 2 == 1

def not_empty(s):
    return s and s.strip()

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("2020-11-17")

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

def fib2(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(b)
        a, b = b, a+b
    return result

class MyClass():
    def __init__(self):
        self.data = []

Money = 2000

def AddMoney():
    global Money
    Money += 1

def fileStudy():
    fo = open('foo.txt', 'w')
    print('文件名：', fo.name)
    print('是否已关闭：', fo.closed)
    print('访问模式：', fo.mode)
    # 注意：softspace 属性在 Python 3 中已移除
    fo.close()

def testTry():
    try:
        fh = open("testfile", "w")
        fh.write("测试文件，用于测试异常")
    except IOError:
        print("Error: 没有找到文件或者读取文件失败")
    else:
        print("内容写入文件成功")
        fh.close()

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    
    def displayEmpoyee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


def employee_test():
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    emp1.displayEmpoyee()
    emp2.displayEmpoyee()
    print("Total Employee  %d" % Employee.empCount)

    hasattr(emp1, 'age')
    setattr(emp1, 'age', 9)
    getattr(emp1, 'age')
    delattr(emp1, 'age')

    print('Employee.__doc__:', Employee.__doc__)
    print('Employee.__name__:', Employee.__name__)
    print('Employee.__module__:', Employee.__module__)
    print('Employee.__bases__:', Employee.__bases__)
    print('Employee.__dict__:', Employee.__dict__)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, '销毁')

def point_test():
    pt1 = Point()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt2))
    del pt1
    del pt2
    del pt3

class Parent:
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")
    
    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性:", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")

def class_test():
    c = Child()
    c.childMethod()
    c.parentMethod()
    c.setAttr(200)
    c.getAttr()


# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

def vector_test():
    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print(v1 + v2)


class JustCounter:
    __secretCount = 0 # 私有变量
    publicCount = 0   # 公有变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

def just_test():
    counter = JustCounter()
    counter.count()
    counter.count()
    print(counter.publicCount)
    print(counter.__secretCount)

def regex_test():
    print(re.match('www', 'www.runoob.com').span())
    print(re.match('com', 'www.runoob.com'))

    line = "Cats are smarter than dogs"

    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        print("matchObj.group() :", matchObj.group())
        print("matchObj.group(1) :", matchObj.group(1))
        print("matchObj.group(2) :", matchObj.group(2))
    else:
        print("No match!!")

    print(re.search('www', 'www.runoob.com').span())
    print(re.search('com', 'www.runoob.com').span())

    # compile函数用于编译正则表达式，生成一个正则表达式对象
    pattern = re.compile(r'\d+')
    m = pattern.match('one12twothree34four')
    print(m)
    m = pattern.match('one12twothree34four', 2, 10)
    print(m)
    m = pattern.match('one12twothree34four', 3, 10)
    print(m)
    print(m.group(), m.start(), m.end(), m.span())

    pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I) # re.I是忽略大小写
    m = pattern.match('Hello World Wide Web')
    print(m)
    print(m.group(), m.span(), m.group(1), m.span(1), m.group(2), m.span(2), m.groups())

    # findall
    # findall在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
    pattern = re.compile(r'\d+')
    result1 = pattern.findall('runoob 123 google 456')
    result2 = pattern.findall('run88oob123google456', 0, 10)
    print(result1)
    print(result2)

    # finditer返回迭代器
    it = re.finditer(r'\d+', '12a32bc43jf3')
    for match in it:
        print(match.group())
    
    # split能够按照匹配的子串将字符串分割后返回列表
    result = re.split('\W+', 'runoob, runoob, runoob.')
    print(result)

def MySQL_test():
    import MySQLdb
    db = MySQLdb.connect('localhost', 'root', '', 'TESTDB', charset='utf8')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

"""
寻找水仙花数
"""
def findNum():
    res = []
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            res.append(num)
    print(res)

"""
正整数反转
"""
def numReverse(num):
    res = 0
    while num > 0:
        res = res * 10 + num % 10
        num //= 10
    print(res)

"""
百钱百鸡
"""
def moneyAndChicken():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if (5 * x + 3 * y + z / 3.0 == 100):
                print('公鸡：%d只，母鸡：%d只，🐤：%d只' % (x, y, z))
"""
Craps赌博游戏
"""
def craps():
    money = 1000
    while money > 0:
        print('你的总资产为：%d' % money)
        needs_go_on = False
        while True:
            debt = int(input('请下注：'))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜！')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜！')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            time.sleep(1)
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('专家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了，游戏结束!')

"""
找出10000以内的完美数
"""
def perfectNum():
    res = []
    for num in range(1, 10000):
        result = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                result += factor
                if factor != 1 and num // factor != factor:
                    result += num // factor
        if result == num:
            res.append(num)
    print(res)

"""
输出2~99之间的素数
"""
def prime(high = 100):
    res = []
    for num in range(2, high):
        is_prime = True
        for factor in range(2, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            res.append(num)
    print(res)

"""
最大公约数
"""
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


"""
最小公倍数
"""
def lcm(x, y):
    return x * y // gcd(x, y)


# 判断一个数是否是回文数
def is_palindrome(num):
    temp = num
    cur = 0
    while temp > 0:
        cur = cur * 10 + temp % 10
        temp //= 10
    return cur == num

def is_prime(num):
    """判断一个数是否是素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

def test1():
    from main import DEBUG, debug_init
    print('******test1******')
    print(DEBUG, id(DEBUG))
    debug_init()
    print(DEBUG, id(DEBUG))


def test2():
    import main
    print('******test2******')
    print(main.DEBUG, id(main.DEBUG))
    main.debug_init()
    print(main.DEBUG, id(main.DEBUG))

if __name__ == "__main__":
    # print(str2int('12314123414'))
    # print filter(is_odd, [i for i in range(10)])
    # print(filter(not_empty, ['a', 'b', '', None, 'c', ' ']))
    # f = lazy_sum(1, 3, 5, 7, 9)
    # print(f)
    # print(f())
    # f1, f2, f3 = count()
    # print(f1(), f2(), f3())
    # now()
    # print fib2(10)
    # for x in range(1, 11):
    #     print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
    # print(glob.glob('*.py'))
    # print(date.today())
    # ticks = time.time()
    # localtime = time.localtime(time.time())
    # print ticks
    # print localtime
    # testTry()
    # employee_test()
    # point_test()
    # class_test()
    # vector_test()
    # just_test()
    # regex_test()
    # MySQL_test()
    # findNum()
    # numReverse(123123)
    # moneyAndChicken()
    # craps()
    # perfectNum()
    # prime()
    test1()
    test2()
    print(sys.modules)
