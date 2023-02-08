# BJ 2193

import sys

N = int(sys.stdin.readline())
arr = [[0, 0], [0, 1]]
if N >= 3:
    for i in range(2, N+1):
        arr.append([arr[i-1][0]+arr[i-1][1], arr[i-1][0]])
print(sum(arr[N]))
