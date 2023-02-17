# BJ 4963

import sys
sys.setrecursionlimit(10000)

move = [[1, 0, -1, 0, 1, 1, -1, -1], [0, 1, 0, -1, 1, -1, 1, -1]]


def dfs(y, x):
    arr[y][x] = 0
    for i in range(8):
        new_y = y + move[0][i]
        new_x = x + move[1][i]
        if new_x >= 0 and new_x < X and new_y >= 0 and new_y < Y and arr[new_y][new_x] == 1:
            dfs(new_y, new_x)


while (True):

    X, Y = map(int, sys.stdin.readline().split())
    if Y == 0 and X == 0:
        break

    arr = []

    for i in range(Y):
        temp = list(map(int, sys.stdin.readline().split()))
        arr.append(temp)

    total = 0

    for i in range(Y):
        for j in range(X):
            if arr[i][j] == 1:
                dfs(i, j)
                total += 1

    print(total)
