def solution(x, n):
    answer = []
    cnt = 0
    a = x
    
    while cnt < n :
        answer.append(a)
        a += x
        cnt += 1
    
    return answer
