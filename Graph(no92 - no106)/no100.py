# BJ 7576

import sys
from collections import deque

move = [[1, 0, -1, 0], [0, 1, 0, -1]]


def bfs():
    global max_depth
    q = deque()
    for i in range(Y):
        for j in range(X):
            if arr[i][j] == 1:
                q.append([i, j, 0])
    while q:
        now_y, now_x, depth = q.popleft()
        max_depth = max(depth, max_depth)
        for i in range(4):
            new_y = now_y + move[0][i]
            new_x = now_x + move[1][i]
            if new_x >= 0 and new_x < X and new_y >= 0 and new_y < Y and arr[new_y][new_x] == 0:
                arr[new_y][new_x] = 1
                q.append([new_y, new_x, depth+1])


X, Y = map(int, sys.stdin.readline().split())
arr = []

for i in range(Y):
    arr.append(list(map(int, sys.stdin.readline().split())))

max_depth = 0
possible = True
bfs()
for i in range(Y):
    for j in range(X):
        if arr[i][j] == 0:
            possible = False
            break
    if not possible:
        break

print(max_depth if possible else -1)
