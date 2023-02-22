# BJ 1182

import sys


def dfs(idx, su):
    global ans
    if idx >= N:
        return
    if idx > 0 and su == S:
        ans += 1
    for i in range(idx, N):
        dfs(i+1, su + arr[i])


N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
dfs(0, 0)
print(ans)
