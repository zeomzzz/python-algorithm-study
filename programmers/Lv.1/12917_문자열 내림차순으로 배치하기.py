def solution(s):
    answer = ''
    
    s_sorted = sorted(s, reverse = True)
    
    for i in s_sorted :
        answer += i
    
    return answer
