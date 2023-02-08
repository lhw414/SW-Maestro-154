# BJ 9012

import sys

T = int(sys.stdin.readline())

for tc in range(T):
    stack = []
    str = sys.stdin.readline().rstrip()
    ans = "YES"
    for char in str:
        if char == "(":
            stack.append("(")
        else:
            if not stack:
                ans = "NO"
                break
            if stack.pop() != "(":
                ans = "NO"
                break
    if len(stack) != 0:
        ans = "NO"
    print(ans)
