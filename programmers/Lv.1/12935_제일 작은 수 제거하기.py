def solution(arr):
    answer = []
    min_num = min(arr)
    
    if len(arr) == 1 :
        answer = [-1]
    else :
        arr.remove(min_num)
        answer = arr
    
    return answer
