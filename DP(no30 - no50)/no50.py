# BJ 11052

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    for j in range(0, i):
        arr[i] = max(arr[i], arr[i-j-1] + arr[j])

print(arr[N-1])
