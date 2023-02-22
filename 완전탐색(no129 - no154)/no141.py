# BJ 5014

import sys
from collections import deque


def bfs():
    q = deque()
    q.append(S)
    visited[S] = 1
    while q:
        v = q.popleft()
        if v == G:
            return count[G]
        for i in (v+U, v-D):
            if 0 < i <= F and not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)
    if count[G] == 0:
        return "use the stairs"


F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [0 for i in range(F+1)]
count = [0 for i in range(F+1)]
print(bfs())
