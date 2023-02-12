# BJ 1912

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i, num in enumerate(arr):
    if i == 0:
        continue
    if arr[i-1] + num > num:
        arr[i] += arr[i-1]

print(max(arr))
