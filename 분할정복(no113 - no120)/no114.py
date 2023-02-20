# BJ 1780

import sys


def recursive(start_y, start_x, size):
    global countMOne, countZero, countOne
    # check 1
    notOne = False
    for i in range(start_y, start_y+size):
        for j in range(start_x, start_x+size):
            if arr[i][j] != 1:
                notOne = True
                break
        if notOne:
            break
    if not notOne:
        countOne += 1
        return
    # check 0
    notZero = False
    for i in range(start_y, start_y+size):
        for j in range(start_x, start_x+size):
            if arr[i][j] != 0:
                notZero = True
                break
        if notZero:
            break
    if not notZero:
        countZero += 1
        return
    # check -1
    notMOne = False
    for i in range(start_y, start_y+size):
        for j in range(start_x, start_x+size):
            if arr[i][j] != -1:
                notMOne = True
                break
        if notMOne:
            break
    if not notMOne:
        countMOne += 1
        return
    if notMOne and notOne and notZero:
        if size >= 3:
            for i in range(3):
                for j in range(3):
                    recursive(start_y+(size//3)*i,
                              start_x+(size//3)*j, size//3)


N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

countOne = 0
countZero = 0
countMOne = 0

recursive(0, 0, N)

print(countMOne)
print(countZero)
print(countOne)
