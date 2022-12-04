def solution(s, n):
    answer = ''
    
    for i in s :
        if i == ' ' :
            answer += i
        else :
            ascii_pushed = ord(i) + n
            
            if ord(i) < 91 and ascii_pushed > 90 :
                answer += chr(ascii_pushed - 26)
            elif ascii_pushed > 122 :
                answer += chr(ascii_pushed - 26)
            else :
                answer += chr(ascii_pushed)
    
    return answer
