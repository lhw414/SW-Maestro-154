# BJ 2011

import sys

s = sys.stdin.readline().rstrip()

dp = [[0] * (len(s)), [0] * (len(s))]
dp[0][0] = 1
if (s[0] == "0"):
    print(0)
else:
    for i in range(1, len(s)):
        if s[i] != "0":
            dp[0][i] = dp[0][i-1]+dp[1][i-1]
        if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
            dp[1][i] = dp[0][i-1]
    print((dp[0][len(s)-1] + dp[1][len(s)-1]) % 1000000)
