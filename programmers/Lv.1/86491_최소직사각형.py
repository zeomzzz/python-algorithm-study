# 풀이 1. zip() 이용

def solution(sizes):
    
    for i in sizes :
        i.sort()
    
    a, b = list(zip(*sizes))
    
    answer = max(a) * max(b)
    
    return answer
 

# 풀이 2. min, max와 for문 활용

def solution(sizes):
    
    a = max(max(i) for i in sizes)
    b = max(min(k) for k in sizes)
    answer = a * b
        
    return answer
