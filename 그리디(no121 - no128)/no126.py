# BJ 11399

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
arr.sort()

for i in range(N):
    ans += sum(arr[:i+1])

print(ans)
