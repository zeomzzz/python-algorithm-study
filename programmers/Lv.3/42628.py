# 풀이 2. heapq.nlargest, nsmallest 이용
import heapq

def solution(operations):
    answer = []
    
    pq = []
    heapq.heapify(pq)
    
    for operation in operations :
        if operation[0] == "I" :
            heapq.heappush(pq, int(operation[2:]))
        else :
            if len(pq) > 0 :
                if operation[2] == "1" : 
                    print(heapq.nlargest(1, pq)[0])
                    pq.remove(heapq.nlargest(1, pq)[0])
                else : 
                    heapq.heappop(pq)
    
    if len(pq) > 0 :
        answer.append(heapq.nlargest(1, pq)[0])
        answer.append(heapq.nsmallest(1, pq)[0])
    else :
        answer = [0, 0]
    
    return answer


# 풀이 1. list 이용
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


