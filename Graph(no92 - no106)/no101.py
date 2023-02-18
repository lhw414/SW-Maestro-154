# BJ 2178

import sys
from collections import deque

move = [[1, 0, -1, 0], [0, 1, 0, -1]]


def bfs():
    global max_depth
    q = deque()
    q.append([0, 0, 0])
    visit_list[0][0] = True
    while q:
        now_y, now_x, depth = q.popleft()
        visit_list[now_y][now_x] = True
        if now_y == Y-1 and now_x == X-1:
            max_depth = depth
            break
        for i in range(4):
            new_y = now_y + move[0][i]
            new_x = now_x + move[1][i]
            if new_x >= 0 and new_x < X and new_y >= 0 and new_y < Y and arr[new_y][new_x] == 1 and visit_list[new_y][new_x] == False:
                q.append([new_y, new_x, depth+1])


Y, X = map(int, sys.stdin.readline().split())
arr = []
visit_list = [[False] * X for _ in range(Y)]
for i in range(Y):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))
max_depth = 0
bfs()


print(max_depth+1)
