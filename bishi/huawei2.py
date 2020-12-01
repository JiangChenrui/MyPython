# -*- coding: utf-8 -*-

def findMax(trangel, m, n):
    helpList = [[1] * n for i in range(m)]
    print(helpList)
    ret = 1
    for i in range(m):
        for j in range(n):
            


if __name__ == '__main__':
    line = input()
    inputList = []
    m, n = map(int, line.split())
    for i in range(m):
        line = input()
        if line=='':
            break
        lines = line.split()
        lines = list(map(int, lines))
        inputList.append(lines)
    print(findMax(inputList, m, n))