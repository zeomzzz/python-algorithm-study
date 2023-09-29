# 1. 일단 총 works를 구함
# 2. works <= n 이면 result도 0
# 3. 아니면.. 돌아가면서 -1
import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) > n : 
        pq = []
        heapq.heapify(pq)
        
        for work in works : heapq.heappush(pq, work * (-1))
        
        cnt = 0
        while cnt < n :
            tmp = heapq.heappop(pq) * (-1)
            if tmp != 0 :
                heapq.heappush(pq, (tmp - 1) * (-1))
                cnt += 1
        
        while pq :
            tmp = heapq.heappop(pq)
            answer += tmp ** 2
    
    return answer
