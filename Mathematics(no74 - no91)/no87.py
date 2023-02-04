# BJ 6588

import sys

dp = [1] * (1000000 + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, 1001):
    if dp[i]:
        for j in range(i * i, 1000001, i): # i의 배수를 지워 나감
            dp[j] = 0

# 같은 에라토스테네스의 체를 구하는 코드이지만, 위와 비교하면 300ms 정도 느림
# for i in range(2, max_val + 1):
#     j = 2
#     while i * j <= max_val:
#         dp[i * j] = 0
#         j += 1

def check_goldbach(n):
    for i in range(2, n):
        if dp[i] and dp[n - i]: # e.g. 20 = 3 (i) + 17 (n - i)
            print(f'{n} = {i} + {n - i}')
            return 0 # 0을 return 하면서 지정된 문자열을 출력하지 못하게 함
    return 1 # 골드바흐의 추측에 부합하지 않으므로 지정된 문자열을 출력

while 1:
    try:
        n = int(sys.stdin.readline())
        if n == 0: # 이거 안해주면 런타임 에러 남...
            break
        if check_goldbach(n): # return 값에 따라 아래 문자열 출력
            print("Goldbach's conjecture is wrong.")
    except EOFError:
        break