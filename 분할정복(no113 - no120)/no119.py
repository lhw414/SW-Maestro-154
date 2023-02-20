# BJ 1517

import sys


def merge_sort(start, end):
    global swap_count, A

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if A[a] <= A[b]:
                temp.append(A[a])
                a += 1
            else:
                temp.append(A[b])
                b += 1
                swap_count += (mid - a + 1)

        if a <= mid:
            temp = temp + A[a:mid + 1]
        if b <= end:
            temp = temp + A[b:end + 1]

        for i in range(len(temp)):
            A[start + i] = temp[i]


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

swap_count = 0
merge_sort(0, N - 1)
print(swap_count)
