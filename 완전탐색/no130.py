#BJ 1107

channel = int(input())
M = int(input())
if M>0:
    breakedButton = list(input().split())
else:
    breakedButton = []

minMove = abs(channel - 100)

for nums in range(1000001):
    nums = str(nums)

    for idx, num in enumerate(nums):
        if num in breakedButton:
            break
        
        elif idx == len(nums) - 1:
            minMove = min(minMove, abs(int(nums) - channel) + len(nums))
print(minMove)
