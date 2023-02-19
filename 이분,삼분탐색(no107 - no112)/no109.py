# BJ 2110

import sys


def binary_search(array, start, end):
    while (start <= end):
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= C:
            global answer
            start = mid+1
            answer = mid
        else:
            end = mid-1


N, C = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

start, end = 1, arr[-1] - arr[0]
answer = 0

binary_search(arr, start, end)
print(answer)
