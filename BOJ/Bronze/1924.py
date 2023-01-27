x, y = map(int, input().split())

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] # 날 수 % 7 의 나머지에 따라 요일 결정됨
d = 0

# x - 1 월까지의 날  수
if x != 1 :
  for i in range(1, x) :
    if i in [1, 3, 5, 7, 8, 10, 12] :
      d += 31
    elif i == 2 :
      d += 28
    else :
      d += 30

# 해당 월의 일을 더함
d += y

print(days[d % 7])
