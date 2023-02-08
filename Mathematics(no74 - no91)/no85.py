# BJ 1978

prime = [True for _ in range(1001)]

prime[1] = False

for i in range(2, 102):
    if prime[i]:
        for j in range(2*i, 1001, i):
            prime[j] = False

N = int(input())
arr = list(map(int, input().split()))
ans = 0

for num in arr:
    if prime[num]:
        ans += 1

print(ans)
