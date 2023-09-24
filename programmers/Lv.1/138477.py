import heapq

def solution(k, score):
    answer = []
    scores = []
    heapq.heapify(scores)
    
    for s in score :

        if len(scores) < k :
            heapq.heappush(scores, s)
        
        elif s > min_score :
            heapq.heappop(scores)
            heapq.heappush(scores, s)
            
        min_score = heapq.heappop(scores)
        heapq.heappush(scores, min_score)
        
        answer.append(min_score)
            
    return answer
