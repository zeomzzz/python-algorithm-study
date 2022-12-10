def solution(s):
    answer = [-1]
    
    for i in range(1, len(s)) :
        s1 = s[:i]
        
        # s[i]가 s[i] 이전에 있으면
        if s[i] in s1 :
            d = 0
            
            while True :
                if s[i] == s1[len(s1)-d-1:len(s1)-d] :
                    answer.append(d+1)
                    break
                d += 1
        else :
            answer.append(-1)
    
    return answer
