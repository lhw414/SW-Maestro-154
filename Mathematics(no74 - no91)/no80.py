# BJ 2745

N, B = input().split()
B = int(B)
ans = 0

for idx, num in enumerate(N):
    if "A"<=num and num<="Z":
        ans += (ord(num)-ord("A") + 10) * (B ** (len(N)-idx-1))
    else:
        ans += int(num) * (B ** (len(N)-idx-1))

print(ans)