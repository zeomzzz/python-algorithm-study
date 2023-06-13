def solution(n):
    answer = 0
    while True :
        if n / 7 == int(n/7) :
            answer = n/7
            break
        else :
            answer = int(n/7) + 1
            break
    return answer
