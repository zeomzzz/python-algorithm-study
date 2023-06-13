def solution(my_str, n):
    answer = []
    
    for i in range(int(len(my_str)/n)) :
        str_sliced = ''
        str_sliced = my_str[n * i : n * i + n]
        answer.append(str_sliced)
        
    if len(my_str) % n != 0 :
        last_sliced = my_str[n * i + n : len(my_str)]
        answer.append(last_sliced)
        
    return answer
