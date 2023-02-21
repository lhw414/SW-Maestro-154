# BJ 1931

import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
current_finish_time = 0
idx = 1
count = 1
end_time = arr[0][1]
for i in range(1, N):
    if arr[i][0] >= end_time:
        count += 1
        end_time = arr[i][1]

print(count)
