# BJ 10814

import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(sys.stdin.readline().split()))
so.sort(key=lambda x: x[0])
for i in so:
    print(i[0], i[1])