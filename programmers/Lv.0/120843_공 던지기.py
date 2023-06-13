def solution(numbers, k):

    tmp = []
    
    if len(numbers) % 2 == 0 :
        
        for i in range(0, len(numbers)//2) :
            tmp.append(i*2)
        
        tmp_index = (k-1) % (len(numbers)//2)
        answer = tmp[tmp_index] + 1
    
    else :
        for i in range(0, len(numbers)//2 + 1) :
            tmp.append(i*2)
        
        for i in range(0, len(numbers)//2) :
            tmp.append(i*2 + 1)
        
        tmp_index = (k-1) % len(numbers)
        answer = tmp[tmp_index] + 1
        
    return answer
