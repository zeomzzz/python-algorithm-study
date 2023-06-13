def solution(my_string):
    answer = []
    for i in range(0, len(my_string)) :
        a = my_string[i]
        if a.isdigit() :
            a = int(a)
            answer.append(a)
    answer.sort()
    return answer
