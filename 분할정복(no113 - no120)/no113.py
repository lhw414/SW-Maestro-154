# BJ 11728

import sys

N, M = map(int, sys.stdin.readline().split())

arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

i = j = 0

while (i < N and j < M):
    if arr1[i] < arr2[j]:
        print(arr1[i], end=" ")
        i += 1
    elif arr1[i] > arr2[j]:
        print(arr2[j], end=" ")
        j += 1
    elif arr1[i] == arr2[j]:
        print(arr1[i], end=" ")
        print(arr2[j], end=" ")
        i += 1
        j += 1

if i < N:
    for k in range(i, N):
        print(arr1[k], end=" ")

if j < M:
    for k in range(j, N):
        print(arr2[j], end=" ")
