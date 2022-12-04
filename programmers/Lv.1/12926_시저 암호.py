def solution(s, n):
    answer = ''
    
    for i in s :
        if i == ' ' :
            answer += i
        else :
            ascii_pushed = ord(i) + n
            
            if i.isupper() and ascii_pushed > ord("Z") :
                answer += chr(ascii_pushed - 26)
            elif i.islower() and ascii_pushed > ord("z") :
                answer += chr(ascii_pushed - 26)
            else :
                answer += chr(ascii_pushed)
    
    return answer
