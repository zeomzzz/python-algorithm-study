def solution(order):
    answer = 0
    while True :
        if order%10 in (3, 6, 9) :
            answer += 1
            order = (order - order%10)/10
        elif order == 0 :
            break
        else :
            order = (order - order%10)/10
    return answer
