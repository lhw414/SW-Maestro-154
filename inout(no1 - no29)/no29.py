# BJ 10992

N = int(input())

for i in range(N):
    if i == 0:
        print(" "*(N-i-1), end="")
        print("*")
    elif i == N-1:
        print("*"*(2*i+1))
    else:
        print(" "*(N-i-1), end="")
        print("*", end="")
        print(" "*(2*i-1), end="")
        print("*")
