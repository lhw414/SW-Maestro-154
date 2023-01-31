# BJ 1463

N = int(input())

ans = 0

def calc(n):
    print("calc")
    global ans
    if n == 1:
        return
    elif n%3 == 0:
        ans += 1
        calc(n//3)
        return
    elif n%2 == 0:
        ans += 1
        calc(n//2)
        return
    else:
        ans += 1
        calc(n-1)
        return

calc(N)

print(ans)