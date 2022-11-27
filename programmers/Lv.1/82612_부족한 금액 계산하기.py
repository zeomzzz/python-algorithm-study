def solution(price, money, count):
    
    total_cnt = (count * (count + 1)) / 2
    total_price = total_cnt * price
    
    answer = total_price - money
    
    if answer < 0 : answer = 0

    return answer
