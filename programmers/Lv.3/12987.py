def solution(A, B):
    answer = 0
    
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    for a in A :
        if len(B) == 0 : break
        
        if B[0] > a :
            B.pop(0)
            answer += 1
    
    return answer
