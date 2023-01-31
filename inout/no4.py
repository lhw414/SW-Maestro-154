# BJ 10950

a = int(input())
b=[]

for i in range(a):
    c,d = map(int, input().split())
    b.append(c+d)

for num in b:
    print(num)
    