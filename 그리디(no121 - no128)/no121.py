# BJ 11047

import sys

N, K = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(N)]
count = 0

for i in range(N-1, -1, -1):
    remain = K//arr[i]
    if (remain >= 1):
        K -= arr[i] * remain
        count += remain

print(count)
