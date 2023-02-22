# BJ 3108

import sys

n = int(sys.stdin.readline())
position = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
group = [0] * 1001
gid = 0
visit = {}


def change(g1, g2):
    h1, h2 = g1, g2
    while h1 != group[h1]:
        h1 = group[h1]
    while h2 != group[h2]:
        h2 = group[h2]
    if h1 == h2:
        return
    else:
        group[h2] = h1


for x1, y1, x2, y2 in position:
    gid += 1
    group[gid] = gid
    for i in range(y1, y2+1):
        if visit.get((i, x1)):
            change(gid, visit[(i, x1)])
        if visit.get((i, x2)):
            change(gid, visit[(i, x2)])
        visit[(i, x1)] = gid
        visit[(i, x2)] = gid
    for j in range(x1+1, x2):
        if visit.get((y1, j)):
            change(gid, visit[(y1, j)])
        if visit.get((y2, j)):
            change(gid, visit[(y2, j)])
        visit[(y1, j)] = gid
        visit[(y2, j)] = gid

cnt = 0
for i in range(1, 1001):
    if i == group[i]:
        cnt += 1

if visit.get((0, 0)):
    cnt = cnt-1 if cnt > 0 else 0
print(cnt)
