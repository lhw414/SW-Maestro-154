# BJ 2156

import sys

t = int(sys.stdin.readline())
s = []
ans = []
for i in range(t):
    s.append(int(sys.stdin.readline()))
for i in range(3):
    ans.append([0]*t)
ans[0][0], ans[1][0], ans[2][0] = 0, s[0], 0
for i in range(1, t):
    ans[0][i] = max(ans[0][i-1], ans[1][i-1], ans[2][i-1])
    ans[1][i] = ans[0][i-1] + s[i]
    ans[2][i] = ans[1][i-1] + s[i]
print(max(ans[0][t-1], ans[1][t-1], ans[2][t-1]))
