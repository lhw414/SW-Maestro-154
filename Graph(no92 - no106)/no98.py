# BJ 2667

import sys
sys.setrecursionlimit(10000)

move = [[1, 0, -1, 0], [0, 1, 0, -1]]


def dfs(y, x):
    global count
    arr[y][x] = "0"
    count += 1
    for i in range(4):
        new_y = y + move[0][i]
        new_x = x + move[1][i]
        if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N and arr[new_y][new_x] == "1":
            dfs(new_y, new_x)


N = int(sys.stdin.readline())
arr = []

for i in range(N):
    temp = sys.stdin.readline()
    tempArr = []
    for s in temp:
        tempArr.append(s)
    arr.append(tempArr)

ans = []
total = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == "1":
            count = 0
            dfs(i, j)
            total += 1
            ans.append(count)

ans.sort()
print(total)
for answer in ans:
    print(answer)
