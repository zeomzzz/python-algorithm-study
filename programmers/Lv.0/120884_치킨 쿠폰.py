def solution(chicken):
    answer = 0
    coupon = chicken

    while True :
        answer += coupon // 10
        coupon = coupon // 10 + coupon % 10
        
        if coupon < 10 :
            break
        
    return answer
