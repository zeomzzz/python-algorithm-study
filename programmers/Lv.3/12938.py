def solution(n, s):
    answer = []
    
    if s < n : 
        answer = [-1]
    else :
        a = s // n
        b = s % n
        
        for i in range(n) :
            if b != 0 :
                answer.append(a + 1)
                b -= 1
            else :
                answer.append(a)
        
        answer.sort()
    
    return answer
