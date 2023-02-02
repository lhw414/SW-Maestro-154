# BJ 11655

s = input()
ans = ""

for c in s:
    if 'a' <= c <= 'z':
        ans += chr((ord(c)+13) if c <= 'm' else ord(c)-13)
    elif 'A' <= c <= 'Z':
        ans += chr((ord(c)+13) if c <= 'M' else ord(c)-13)
    else:
        ans += c
print(ans)