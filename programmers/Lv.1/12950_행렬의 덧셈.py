# 풀이 1. 인덱싱하여 더함

def solution(arr1, arr2):
    len_row = len(arr1)
    len_col = len(arr1[0])
    
    for i in range(0, len_row) :
        for k in range(0, len_col) :
            arr1[i][k] += arr2[i][k]
    
    return arr1
 

# 풀이 2. zip, map 이용
def solution(arr1, arr2):
    answer = []
    
    for args in zip(arr1, arr2) :
        answer.append(list(map(sum, zip(*args))))
    
    return answer
