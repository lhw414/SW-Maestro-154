# BJ 1963

import copy
from collections import deque

test_case = int(input())
primeArr = [True for _ in range(10000)]

for i in range(2, 100): # 제곱근 범위까지
        if primeArr[i] == True:
            for j in range(2*i, 10000, i):
                primeArr[j] = False

def bfs():
    q = deque()
    q.append([N, 0])

    visitied = [0 for _ in range(10000)]
    visitied[N] = 1

    while q:
        now, cnt = q.popleft()
        strNow = str(now)

        if now == M:
            return cnt
        
        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i+1:])
                if visitied[temp] == 0 and primeArr[temp] == True and temp >= 1000:
                    visitied[temp] = 1
                    q.append([temp, cnt + 1]) 

for T in range(test_case):
    N, M = map(int, input().split())
    result = bfs()
    print(result if result != None else "Impossible")
