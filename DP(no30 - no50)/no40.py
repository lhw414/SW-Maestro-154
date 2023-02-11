# BJ 11055

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = arr[:]
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            ans[i] = max(ans[i], ans[j] + arr[i])

print(max(ans))
