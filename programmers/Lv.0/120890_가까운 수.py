def solution(array, n):
    
    while True :
        if abs(n - array[0]) < abs(n - array[1]) :
            del array[1]
        elif abs(n - array[0]) > abs(n-array[1]) :
            del array[0]
        else :
            if array[0] < array[1] :
                del array[1]
            else :
                del array[0]
        
        if len(array) == 1 :
            break
        
    answer = array[0]
    
    return answer
