def solution(my_string):
    answer = ''
    
    answer += my_string[0]
    
    for i in range(1, len(my_string)) :
        if my_string.count(my_string[i], 0, i) == 0 :
            answer += my_string[i]
    
    return answer
