# BJ 11576

A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
temp = 0

for i in range(m):
    temp += arr[i] * (A ** (m-i-1))

res = ""

while(temp>0):
    res = str(temp%B) + " " + res
    temp = temp//B

print(res)