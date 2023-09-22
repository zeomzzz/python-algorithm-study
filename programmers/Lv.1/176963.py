def solution(name, yearning, photo):
    answer = []
    
    dic = {}
    for i in range(len(name)) : dic[name[i]] = yearning[i]
    
    for tmp in photo :
        score = 0
        for t in tmp :
            if t in dic :
                score += dic[t]
        answer.append(score)
    
    return answer
