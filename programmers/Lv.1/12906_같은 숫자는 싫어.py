def solution(arr):
    
    answer = [arr[0]]
    
    for i in arr :
        if answer[len(answer) - 1] != i :
            answer.append(i)
    
    return answer
