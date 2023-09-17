def solution(s):
    answer = ''
    
    isUpper = True
    for i in range(len(s)) :
        if s[i] == " " :
            isUpper = True
            answer += " "
        else :
            if isUpper :
                answer += s[i].upper()
                isUpper = False
            else :
                answer += s[i].lower()
    
    return answer
