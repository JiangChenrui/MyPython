# -*- coding: utf-8 -*-
import sys
import time


def str2time(str):
    h, m, s = str[:-2].split(':')
    h, m, s = int(h), int(m), int(s)
    if str[-2:] == 'PM':
        h += 12
    elif str[-2:] == 'AM' and h < 5:
        h += 24
    return h, m, s
        

def getEarlyPerson(clockTable):
    person = []
    min = 24 * 60 * 60
    for item in clockTable:
        h, m, s = str2time(item[1])
        sub = (h - 5) * 60 + m * 60 + s
        if min > sub:
            person = []
            person.append(item[0])
            min = sub
        elif min == sub:
            person.append(item[0])
    return person

def getLatePerson(clockTable):
    person = []
    min = 29 * 60 * 60
    for item in clockTable:
        h, m, s = str2time(item[2])
        sub = (29 - h) * 60 + m * 60 + s
        if min > sub:
            person = []
            person.append(item[0])
            min = sub
        elif min == sub:
            person.append(item[0])
    return person


if __name__ == '__main__': 
    inputList = []
    while True:
        list1 = sys.stdin.readline().strip()
        if list1 == '':
            break
        list1 = list(list1.split())
        inputList.append(list1)
    for item in getEarlyPerson(inputList):
        print(item, end=' ')
    print()
    for item in getLatePerson(inputList):
        print(item, end=' ')
    print()
