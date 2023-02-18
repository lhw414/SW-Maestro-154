# BJ 1167

import sys
sys.setrecursionlimit(10000)

v = int(sys.stdin.readline())
graph = [[] for i in range(v+1)]
ans = 0


def dfs(V, size):
    global ans
    ans = max(ans, size)
    visit_list[V] = True
    for tp in graph[V]:
        if not visit_list[tp[0]]:
            dfs(tp[0], size+tp[1])


for i in range(v):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range((len(temp)-2)//2):
        graph[temp[0]].append([temp[2*j+1], temp[2*j+2]])

for i in range(1, v+1):
    visit_list = [True] + [False] * v
    dfs(i, 0)

print(ans)
