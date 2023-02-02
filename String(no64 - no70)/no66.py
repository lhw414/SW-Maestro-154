# BJ 10820

import sys

while(1):
    string = sys.stdin.readline().rstrip('\n')
    if not string:
        break
    ans = [0, 0, 0, 0] #lower, upper, digit, space
    for char in string:
        if char.islower():
            ans[0] += 1
        elif char.isupper():
            ans[1] += 1
        elif char == " ":
            ans[3] += 1
        else:
            ans[2] += 1
    for answer in ans:
        print(answer, end=" ")
    print()