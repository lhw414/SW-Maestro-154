# BJ 1676

from sys import stdin


def fac(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N * fac(N-1)


num = int(stdin.readline())
num = fac(num)
num = str(num)[::-1]

for idx, ch in enumerate(num):
    if ch != "0":
        print(idx)
        break
