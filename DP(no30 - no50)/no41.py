# BJ 11722

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] < arr[j] and ans[i] < ans[j]:
            ans[i] = ans[j]
    ans[i] += 1

print(max(ans))
