def solution(score):
    answer = []
    avg = []
    
    for i in score :
        avg.append((i[0] + i[1]) / 2)
    
    avg_sorted = avg.copy()
    avg_sorted.sort(reverse = True)
    
    for j in avg :
        answer.append(avg_sorted.index(j) + 1)
    
    return answer
