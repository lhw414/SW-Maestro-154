# BJ 1924

Day = 0
DayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x-1):
    Day = Day + DayList[i]
Day = (Day+y)%7

print(weekList[Day])