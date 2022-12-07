# 풀이 1

def solution(a, b):
    month_lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_lst = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    day = b
    i = 0
    
    while i < a - 1 :
        day += month_lst[i]
        i += 1

    return day_lst[day % 7]
  

# 풀이 2 : sum 이용하여 list 요소의 합 구함

def solution(a, b):
    month_lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_lst = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    return day_lst[(sum(month_lst[:a-1]) + b) % 7]
