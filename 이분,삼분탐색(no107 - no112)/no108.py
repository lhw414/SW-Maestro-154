# BJ 2805

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    length = 0
    for i in tree:
        if i >= mid:
            length += i - mid

    if length >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
