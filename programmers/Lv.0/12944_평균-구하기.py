def solution(arr):
    answer = 0
    
    for i in range(len(arr)) :
        answer += arr[i] / len(arr)
        
    return answer
