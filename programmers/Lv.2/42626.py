import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True :
        a = heapq.heappop(scoville) # 제일 작은 음식
        
        if a >= K : break # 제일 작은 것도 K 이상이면 종료
        
        if len(scoville) == 0 : # heapq 비면 K 이상 못 넘기는 경우임
            answer = -1
            break
        
        b = heapq.heappop(scoville) # 두 번째로 작은 음식
        
        heapq.heappush(scoville, a + 2 * b)
        answer += 1
    
    return answer
