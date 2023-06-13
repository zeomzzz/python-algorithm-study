def solution(my_string):
    answer = 0
    
    import re
    
    tmp_list = re.findall(r'\d+', my_string)
    
    for i in tmp_list :
        answer += int(i)
    
    return answer
