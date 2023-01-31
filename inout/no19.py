# BJ 10818

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

print(f'{arr[0]} {arr[-1]}')