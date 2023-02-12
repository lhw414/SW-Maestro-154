# BJ 2133

import sys

N = int(sys.stdin.readline())

arr = [0 for _ in range(N+1)]
arr[2] = 3
if N > 2:
    for i in range(3, N+1):
        if i % 2 == 0:
            arr[i] = arr[i-2] * 3 + sum(arr[:i-2]) * 2 + 2
        else:
            arr[i] = 0

print(arr[N])
