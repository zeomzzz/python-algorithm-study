def solution(a, b):
    
    # 1) 기약분수 만들기
    for i in range(2, a + 1) :
        if a % i == 0 and b % i == 0 :
            a /= i
            b /= i
    
    # 2) 2, 5로 나누어서 2, 5 외의 소인수 유무 확인
    while True :
        if b % 2 == 0 :
            b /= 2
        else :
            break
    
    while True :
        if b % 5 == 0 :
            b /= 5
        else :
            break
    
    if b == 1 :
        answer = 1
    else :
        answer = 2
    
    return answer
