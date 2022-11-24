def solution(x):
    x_tmp = x
    x_sum = 0
    
    while x_tmp > 0 :
        x_sum += x_tmp % 10
        x_tmp = x_tmp // 10
    
    if x % x_sum == 0 :
        answer = True
    else :
        answer = False
        
    return answer
