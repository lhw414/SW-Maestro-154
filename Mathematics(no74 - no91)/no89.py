# BJ 10872

from sys import stdin

def fac(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N * fac(N-1)

num = int(stdin.readline())

print(fac(num))