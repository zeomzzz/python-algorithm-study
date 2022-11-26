def solution(s):
    mid_index = len(s) // 2
    
    if len(s) % 2 == 1 :
        answer = s[mid_index : mid_index + 1]
    else :
        answer = s[mid_index - 1 : mid_index + 1]
        
    return answer
