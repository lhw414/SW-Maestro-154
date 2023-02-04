# BJ 11653

from sys import stdin
import math

N = int(stdin.readline())
if N == 1:
    print(1)
for i in range(2, int(math.sqrt(N))):
    while(N%i==0):
        print(i)
        N //= i
if N != 1:
    print(N)
