#BJ 11005

N, B = map(int ,input().split())

ans = ""

while(N>0):
    remainder = N%B
    N = N//B
    if remainder>=10:
        ans = chr(ord("A")+remainder-10) + ans
    else:
        ans = str(remainder) + ans
    
print(ans)