def solution(k, m, score):
    answer = 0
    
    score.sort()
    
    while len(score) >= m :
        min_score = 0
        
        box = []
        for i in range(m) :
            tmp = score.pop()
            box.append(tmp)
            
            if i == m-1 : min_score = tmp
        
        answer += m * tmp
    
    return answer
