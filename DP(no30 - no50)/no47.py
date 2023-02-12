# BJ 9461

import sys

arr = [0 for _ in range(101)]
arr[1] = arr[2] = arr[3] = 1
arr[4] = arr[5] = 2
arr[6] = 3

for i in range(7, 101):
    arr[i] = arr[i-1] + arr[i-5]

N = int(sys.stdin.readline())
for i in range(N):
    print(arr[int(sys.stdin.readline())])
