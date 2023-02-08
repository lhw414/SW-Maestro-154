# BJ 10799

import sys

stack = []
str = sys.stdin.readline().rstrip()
ans = 0
for idx, char in enumerate(str):
    if char == "(":
        stack.append("(")
    else:
        if str[idx-1] == "(":
            stack.pop()
            ans += len(stack)
        elif len(stack) != 0:
            stack.pop()
            ans += 1
        else:
            stack.pop()
print(ans)
