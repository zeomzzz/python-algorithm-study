def solution(sequence, k):
    answer = []
    
    start = end = 0
    array_sum = sequence[0]
    l = len(sequence)
    
    while True :
        if array_sum <= k :
            if array_sum == k :
                if len(answer) == 0 : answer = [start, end]
                elif end - start < answer[1] - answer[0] : answer = [start, end]
            
            if end >= l - 1 : break
        
            end += 1
            array_sum += sequence[end]
        
        else :
            # array_sum > k :
            array_sum -= sequence[start]
                
            if start >= l - 1 : break
                
            start += 1
            
    return answer
