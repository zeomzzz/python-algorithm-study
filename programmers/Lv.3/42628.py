def solution(operations):
    answer = []
    
    is_sorted = False
    
    pq = []
    
    for operation in operations :
        cmd, num = operation.split(" ")
        num = int(num)
        
        if cmd == "I" :
            pq.append(num)
            is_sorted = False
        else :
            if not is_sorted : pq.sort()
            if num == 1 :
                if len(pq) > 0 : del pq[-1]
            else :
                if len(pq) > 0 : del pq[0]
    
    if len(pq) > 0 :
        pq.sort()
        answer.append(pq[-1])
        answer.append(pq[0])
    else :
        answer = [0, 0]
    
    return answer
