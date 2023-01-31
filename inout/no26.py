# BJ 2445

N = int(input())

for i in range(N):
    print(" "*(N-i-1), end="")
    print("*"*(i+1))
for i in range(N-2, -1, -1):
    print(" "*(N-i-1), end="")
    print("*"*(i+1))
