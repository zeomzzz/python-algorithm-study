def solution(n):
    answer = []
    
    for i in range(2, n+1) :
        if n % i == 0 :
            answer.append(i)
    
    for j in answer :
        for k in range(2, 5000) :
            if j * k in answer :
                answer.remove(j * k)
    
    return answer
