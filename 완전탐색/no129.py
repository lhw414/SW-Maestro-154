# BJ 1476

E, S, M = map(int, input().split())

year = 1
now_e, now_s, now_m = 1, 1, 1

while(1):
    if now_e == E and now_m == M and now_s == S:
        break
    now_e, now_m, now_s = now_e%15 + 1, now_m%19 + 1, now_s%28 + 1
    year += 1

print(year)
