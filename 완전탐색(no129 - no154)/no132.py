# BJ 10819

import itertools

N = int(input())
arr = list(map(int, input().split()))
nPr = itertools.permutations(arr, N)

maxAns = 0

for permu in nPr:
    currAns = 0
    for j in range(N-1):
        currAns += abs(permu[j] - permu[j+1])
    maxAns = max(maxAns, currAns)

print(maxAns)
