def solution(my_string):
    answer = ''
    for i in range(len(my_string)) :
        j = my_string[i]
        if j not in ['a', 'e', 'i', 'o', 'u'] :
            answer += j
    return answer
