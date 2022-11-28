def solution(arr):
    
    answer = []
    
    for i in arr :
        if answer[-1:] != [i] : # answer[-1:] 로 answer 의 마지막 요소와 비교
            answer.append(i)
    
    return answer
