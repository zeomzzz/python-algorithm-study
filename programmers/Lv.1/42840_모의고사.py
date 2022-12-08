def solution(answers):
    answer = []
    score_lst = []
    lst = [[1, 2, 3, 4, 5], 
           [2, 1, 2, 3, 2, 4, 2, 5], 
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i in lst :
        score = 0
        for j in range(len(answers)) :
            if answers[j] == i[j % len(i)] :
                score += 1
        score_lst.append(score)
    
    for k in range(3) :
        if score_lst[k] == max(score_lst) :
            answer.append(k+1)
    
    return answer
