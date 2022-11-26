def solution(left, right):
    
    # 약수의 개수가 홀수 : 어떤 정수의 거듭제곱
    
    answer = 0
    
    for i in range(left, right + 1) :
        if int(i ** (1 / 2)) == i ** ( 1 / 2 ) :
            answer -= i
        else :
            answer += i
    
    return answer
