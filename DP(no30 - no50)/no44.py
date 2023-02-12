# BJ 2579

import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

ans = [[0 for _ in range(N)], [0 for _ in range(N)], [0 for _ in range(N)]]
ans[1][0] = arr[0]
for i in range(1, N):
    ans[0][i] = max(ans[1][i-1], ans[2][i-1])
    ans[1][i] = ans[0][i-1] + arr[i]
    ans[2][i] = ans[1][i-1] + arr[i]

print(max(ans[1][N-1], ans[2][N-1]))
