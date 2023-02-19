# BJ 10815

import sys

N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()
temp = sorted(arr2)
num = {}

i = j = 0
while (j < M and i < N):
    if arr1[i] == temp[j]:
        num[temp[j]] = 1
        i += 1
        j += 1
    elif arr1[i] > temp[j]:
        num[temp[j]] = 0
        j += 1
    elif arr1[i] < temp[j]:
        i += 1

if j != M:
    for k in range(j, M+1):
        num[temp[j]] = 0

for n in arr2:
    print(num[n], end=" ")
