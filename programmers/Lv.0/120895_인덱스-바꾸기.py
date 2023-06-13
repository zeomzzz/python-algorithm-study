def solution(my_string, num1, num2):
    answer = ''
    list_my_string = list(my_string)
    
    [list_my_string[num1], list_my_string[num2]] = [list_my_string[num2], list_my_string[num1]]
    
    for i in range(len(list_my_string)) :
        answer += list_my_string[i]
    
    return answer
