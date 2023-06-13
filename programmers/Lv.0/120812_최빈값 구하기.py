def solution(array):
    answer = 0
    i = 0
    tmp_array = []
    array_cnt = []
    
    if len(array) == 1 :
        answer = array[0]
    else :
        
        while len(tmp_array) < len(array) :
            if array[i] not in tmp_array :
                array_cnt.append(1)
            else :
                cnt = tmp_array.count(array[i])
                array_cnt.append(cnt + 1)
            
            tmp_array.append(array[i])
            i += 1
        
        cnt_max = max(array_cnt)
        
        if array_cnt.count(cnt_max) > 1 :
            answer = -1
        else :
            answer = array[array_cnt.index(cnt_max)]
    
    return answer
