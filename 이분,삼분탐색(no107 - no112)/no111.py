# BJ 10816

import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()
dicton = {}
for num in card:
    if num in dicton:
        dicton[num] += 1
    else:
        dicton[num] = 1


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(dicton[check[i]], end=' ')
    else:
        print(0, end=' ')
