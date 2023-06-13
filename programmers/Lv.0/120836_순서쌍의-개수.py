def solution(n):        
    answer = 0
    i = 1
    
    while True :
        if i <= (n // i) :
            if i * (n // i) == n :
                if i != (n // i) :
                    answer += 2
                else :
                    answer += 1
            i += 1
        else :
            break
    return answer

'''
# 이 코드는 일부 TC에서 코드 무한 로딩.. 왜..?
def solution(n):
    answer = 0
    for i in range(0, n+1) :
        for j in range(0, n+1) :
            if i*j == n :
                answer += 1
    return answer
'''
