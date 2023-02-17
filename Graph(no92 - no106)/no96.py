# BJ 2331

import sys

A, P = map(int, sys.stdin.readline().split())

numSet = set()
discardSet = set()
numSet.add(A)
while (True):
    num = 0
    for s in str(A):
        num += int(s) ** P
    if num in numSet:
        numSet.discard(num)
        discardSet.add(num)
    else:
        if num in discardSet:
            break
        numSet.add(num)
    A = num

print(len(numSet))
