# BJ 2146

import sys
from collections import deque
sys.setrecursionlimit(10**6)

num = int(input())
arr = [list(map(int, input().split())) for _ in range(num)]

ans = sys.maxsize


def dfs(i, j):
    global cnt
    if i < 0 or i >= num or j < 0 or j >= num:
        return False
    if arr[i][j] == 1:
        arr[i][j] = cnt
        for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx = x+i
            ny = y+j
            dfs(nx, ny)
        return True


def bfs(n):
    global ans
    check = [[-1] * num for _ in range(num)]
    q = deque()

    for i in range(num):
        for j in range(num):
            if arr[i][j] == n:
                q.append((i, j))
                check[i][j] = 0
    while q:
        x, y = q.popleft()
        for a, b in (0, -1), (0, 1), (1, 0), (-1, 0):
            nx = x+a
            ny = y+b
            if nx < 0 or nx >= num or ny < 0 or ny >= num:
                continue

            if arr[nx][ny] > 0 and arr[nx][ny] != n:
                ans = min(ans, check[x][y])
                return

            if arr[nx][ny] == 0 and check[nx][ny] == -1:
                check[nx][ny] = check[x][y]+1
                q.append((nx, ny))


cnt = 2
for i in range(num):
    for j in range(num):
        if dfs(i, j) == True:
            cnt += 1

for i in range(2, cnt):
    bfs(i)


print(ans)
