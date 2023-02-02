# BJ 11656

s = input()
arr = []

for i in range(len(s)):
    arr.append(s[i:])

arr.sort()

for word in arr:
    print(word)
