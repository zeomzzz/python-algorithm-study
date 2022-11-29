def solution(s):
    answer = ''
    
    s_split = s.split(' ')
    
    for i in s_split :
        
        cnt = 0
        
        while cnt < len(i) :
            if cnt % 2 == 0 :
                answer += i[cnt].upper()
            else :
                answer += i[cnt].lower()
            cnt += 1
        
        answer += ' '
    
    answer = answer[0:len(answer) - 1] # 마지막 스페이스 제외 
    
    return answer
