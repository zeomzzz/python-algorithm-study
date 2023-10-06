def solution(cards1, cards2, goal):
    answer = "Yes"
    
    while goal :
        tmp = goal.pop(0)
        
        if len(cards1) and cards1[0] == tmp : cards1.pop(0)
        elif len(cards2) and cards2[0] == tmp : cards2.pop(0)
        else : 
            answer = "No"
            return answer
    
    return answer
