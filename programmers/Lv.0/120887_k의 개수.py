def solution(i, j, k):

    tmp_str = ''
    
    for a in range(i, j+1) :
        tmp_str += str(a)
    
    tmp_list = list(tmp_str)
    answer = tmp_list.count(str(k))
    
    return answer
