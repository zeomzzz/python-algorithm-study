def solution(n):
    answer = 0
    str_answer = ''
    
    n_str = str(n)
    n_list = list(n_str)
    n_list = sorted(n_list, reverse = True)
    
    for i in n_list :
        str_answer += i
    
    answer = int(str_answer)
    
    return answer
