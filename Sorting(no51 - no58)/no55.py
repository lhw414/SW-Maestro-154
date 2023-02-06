# BJ 10825

import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(sys.stdin.readline().split()))
so.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in so:
    sys.stdout.write(str(student[0]) + "\n")