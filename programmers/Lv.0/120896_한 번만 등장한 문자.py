def solution(s):
    answer = ''
    tmp_list = []
    
    list_s = list(s)
    unique_s = list(set(list_s))
    
    for i in unique_s :
        if list_s.count(i) == 1 :
            tmp_list.append(i)
    
    tmp_list.sort()
    
    for i in tmp_list :
        answer += i
    
    return answer
