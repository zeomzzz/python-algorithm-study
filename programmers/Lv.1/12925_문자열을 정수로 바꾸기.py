# int() 로 풀기
def solution(s):
    
    answer = int(s)
    
    return answer
  
  
# case 나누어서 풀기
def solution(s):
    
    num = 0
    
    if s[0] == '-' :
        i = len(s) - 1
        i_index = 1
        
        while i > 0 :
            num += int(s[i_index]) * (10 ** (i - 1))
            i_index += 1
            i -= 1
        
        answer = num * (-1)
        
    elif s[0] == '+' :
        j = len(s) - 1
        j_index = 1
        
        while j > 0 :
            num += int(s[j_index]) * (10 ** (j - 1))
            j_index += 1
            j -= 1
        
        answer = num
        
    else :
        
        k = len(s)
        k_index = 0
        
        while k > 0 :
            num += int(s[k_index]) * (10 ** (k - 1))
            k_index += 1
            k -= 1
            
        answer = num
            
    return answer
