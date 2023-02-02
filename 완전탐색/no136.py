# BJ 9019

from collections import deque

def bfs():
    q = deque()
    q.append((start, ""))
    visit = [False for _ in range(10000)]
    while q:
        num, cmd = q.popleft()
        visit[num] = True
        if num == end:
            print(cmd)
            break
        nextNum = (2*num)%10000
        if not visit[nextNum]:
            q.append([nextNum, cmd+"D"])
        nextNum = (num-1)%10000
        if not visit[nextNum]:
            q.append([nextNum, cmd+"S"])
        nextNum = (10*num+(num//1000))%10000
        if not visit[nextNum]:
            q.append([nextNum, cmd+"L"])
        nextNum = (num//10+(num%10)*1000)%10000
        if not visit[nextNum]:
            q.append([nextNum, cmd+"R"])

test_case = int(input())

for T in range(test_case):
    start, end = map(int ,input().split())
    bfs()