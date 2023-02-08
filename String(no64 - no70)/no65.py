# BJ 10809

string = input()
arr = [-1 for _ in range(26)]

for idx, char in enumerate(string):
    if arr[ord(char)-ord('a')] == -1:
        arr[ord(char)-ord('a')] = idx

for i in arr:
    print(i, end=" ")
