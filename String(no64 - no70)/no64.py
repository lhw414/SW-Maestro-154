# BJ 10808

string = input()
arr = [0 for _ in range(26)]

for char in string:
    arr[ord(char)-ord('a')] += 1

for i in arr:
    print(i, end=" ")
