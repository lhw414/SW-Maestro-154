# BJ 11057

N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(0, 10):
    dp[1][i] = 1

MOD = 10007

for i in range(2, N+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(sum(dp[N]) % MOD)
