# BJ 8393

N = int(input())

def sum2one(num):
    if num == 1:
        return 1
    else:
        return num + sum2one(num-1)

print(sum2one(N))