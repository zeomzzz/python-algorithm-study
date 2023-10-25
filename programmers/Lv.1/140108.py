def solution(s):
    answer = 0
    
    x = s[0]
    is_x_cnt = 0
    not_x_cnt = 0
    for i in range(0, len(s)) :
        if s[i] == x : is_x_cnt += 1
        else : not_x_cnt += 1
        
        if is_x_cnt == not_x_cnt :
            answer += 1
            is_x_cnt = 0
            not_x_cnt = 0
            if i + 1 < len(s) :
                x = s[i + 1]
        else :
            if i == len(s) - 1 :
                answer += 1
        
    return answer
