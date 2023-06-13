def solution(emergency):
    answer = []
    
    emergency_sorted = sorted(emergency, reverse = True)
    
    for i in emergency :
        order = emergency_sorted.index(i) + 1
        answer.append(order)
    
    return answer
