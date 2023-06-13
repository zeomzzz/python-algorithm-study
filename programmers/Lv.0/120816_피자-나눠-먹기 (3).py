def solution(slice, n):
    i = 0
    while True :
        if (i * slice) // n == 1 :
            answer = i
            break
        else :
            i += 1
    return answer
