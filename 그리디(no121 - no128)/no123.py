# BJ 10610

import sys


def findBigInteger():
    if (sum(arr) % 3 != 0):
        print(-1)
        return
    if 0 not in arr:
        print(-1)
        return
    arr.sort()
    for i in reversed(arr):
        print(i, end="")


N = sys.stdin.readline().rstrip()
arr = []

for num in str(N):
    arr.append(int(num))

findBigInteger()
