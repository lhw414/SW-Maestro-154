# BJ 1987

import sys

move = [[1, 0, -1, 0], [0, 1, 0, -1]]


def dfs(y, x, cell):
    global ans
    ans = max(ans, cell)
    for i in range(4):
        new_y, new_x = y+move[0][i], x+move[1][i]
        if 0 <= new_y <= R-1 and 0 <= new_x <= C-1:
            if visited[ord(arr[new_y][new_x])-ord("A")] == 0:
                visited[ord(arr[new_y][new_x])-ord("A")] = 1
                dfs(new_y, new_x, cell+1)
                visited[ord(arr[new_y][new_x])-ord("A")] = 0


R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [0 for _ in range(26)]
ans = 0
visited[ord(arr[0][0])-ord("A")] = 1
dfs(0, 0, 1)
print(ans)
