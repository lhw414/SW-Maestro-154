# BJ 11724

import sys
sys.setrecursionlimit(10000)


def dfs(v):
    visit_list[v] = 1
    for i in range(1, n + 1):
        if visit_list[i] == 0 and graph[v][i] == 1:
            dfs(i)


n, m = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

ans = 0

for i in range(1, len(visit_list)):
    if visit_list[i] == 0:
        dfs(i)
        ans += 1

print(ans)
