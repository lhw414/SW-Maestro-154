# BJ 2446

N = int(input())

for i in range(N):
    print(" "*(i), end="")
    print("*"*(2*(N-i-1)+1))
for i in range(N-2, -1, -1):
    print(" "*(i), end="")
    print("*"*(2*(N-i-1)+1))