# BJ 10971

def dfs(start, now, value, cnt):
    global minCost
    if cnt == N:
        if arr[now][start]:
            value += arr[now][start]
            minCost = min(minCost, value)
    
    if value > minCost:
        return

    for i in range(N):
        if not visited[i] and arr[now][i]:
            visited[i] = 1
            dfs(start, i, value + arr[now][i], cnt + 1)
            visited[i] = 0

N = int(input())

minCost = 99999999

cities = []

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(minCost)