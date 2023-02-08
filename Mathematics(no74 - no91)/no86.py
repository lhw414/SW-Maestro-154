# BJ 1929

prime = [True for _ in range(1000001)]

prime[1] = False

for i in range(2, 1001):
    if prime[i]:
        for j in range(2*i, 1000001, i):
            prime[j] = False

N, M = map(int, input().split())

for num in range(N, M+1):
    if prime[num]:
        print(num)
