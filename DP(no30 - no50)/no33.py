# BJ 9095

import sys

T = int(sys.stdin.readline())
ans = [0, 1, 2, 4]
for i in range(4, 12):
    ans.append(ans[i-3] + ans[i-2] + ans[i-1])
for test_case in range(T):
    N = int(sys.stdin.readline())
    print(ans[N])
