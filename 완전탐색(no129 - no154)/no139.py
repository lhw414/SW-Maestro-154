# BJ 2186

# import sys
# from collections import deque

# move = [[1, 0, -1, 0], [0, 1, 0, -1]]


# def bfs():
#     global ans
#     q = deque()
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == word[0]:
#                 q.append([i, j, 0])

#     while q:
#         cur_y, cur_x, idx = q.popleft()
#         for i in range(4):
#             new_y, new_x = cur_y+move[0][i], cur_x+move[1][i]
#             while (0 <= new_y and new_y < N and 0 <= new_x and new_x < M):
#                 if word[idx+1] == arr[new_y][new_x]:
#                     if idx+1 == len(word)-1:
#                         ans += 1
#                     else:
#                         q.append([new_y, new_x, idx+1])
#                 new_y, new_x = new_y+move[0][i], new_x+move[1][i]


# N, M, K = map(int, sys.stdin.readline().split())

# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

# word = sys.stdin.readline().rstrip()
# ans = 0

# bfs()

# print(ans)

import sys


def dfs(y, x, idx):
    global ans
    if idx == len(word):
        ans += 1
        return
    for k in range(4):
        for step in range(1, K+1):
            ny, nx = y+dy[k]*step, x+dx[k]*step
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and arr[ny][nx] == word[idx]:
                visited[ny][nx] = True
                dfs(ny, nx, idx+1)
                visited[ny][nx] = False


N, M, K = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
word = sys.stdin.readline().rstrip()

ans = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        if arr[i][j] == word[0]:
            visited = [[False]*M for _ in range(N)]
            visited[i][j] = True
            dfs(i, j, 1)

print(ans)
