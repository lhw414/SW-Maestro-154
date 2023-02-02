# BJ 9613

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

T = int(input())

for testCase in range(T):
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(1, arr[0]):
        for j in range(i+1, arr[0]+1):
            ans += gcd(arr[i], arr[j])

    print(ans)