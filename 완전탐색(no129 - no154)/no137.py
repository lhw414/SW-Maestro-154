# BJ 1525

from collections import deque

visit = set()

def bfs():
    q = deque()
    q.append([board, initZeroIdx, 0])
    visit.add(board)
    while q:
        brd, zeroIdx, cnt = q.popleft()
        if brd == ans:
            return cnt
        if zeroIdx != 0 and zeroIdx != 3 and zeroIdx != 6:
            newZeroIdx = zeroIdx - 1
            newBoard = brd[:newZeroIdx] + brd[zeroIdx] + brd[newZeroIdx] + brd[zeroIdx+1:]
            if newBoard not in visit:
                q.append([newBoard, newZeroIdx, cnt+1])
                visit.add(newBoard)
        if zeroIdx != 2 and zeroIdx != 5 and zeroIdx != 8:
            newZeroIdx = zeroIdx + 1
            newBoard = brd[:zeroIdx] + brd[newZeroIdx] + brd[zeroIdx] + brd[newZeroIdx+1:]
            if newBoard not in visit:
                q.append([newBoard, newZeroIdx, cnt+1])
                visit.add(newBoard)
        if zeroIdx >= 3:
            newZeroIdx = zeroIdx - 3
            newBoard = brd[:newZeroIdx] + brd[zeroIdx] + brd[newZeroIdx+1:zeroIdx] + brd[newZeroIdx] + brd[zeroIdx+1:]
            if newBoard not in visit:
                q.append([newBoard, newZeroIdx, cnt+1])
                visit.add(newBoard)
        if zeroIdx < 6:
            newZeroIdx = zeroIdx + 3
            newBoard = brd[:zeroIdx] + brd[newZeroIdx] + brd[zeroIdx+1:newZeroIdx] + brd[zeroIdx] + brd[newZeroIdx+1:]
            if newBoard not in visit:
                q.append([newBoard, newZeroIdx, cnt+1])
                visit.add(newBoard)


ans = "123456780"
board = ""
initZeroIdx = -1

for i in range(3):
    boardStr = list(input().split())
    for j in range(3):
        if boardStr[j] == "0":
            initZeroIdx = 3*i + j
        board += boardStr[j]

ans = bfs()

print(ans if ans != None else -1)
