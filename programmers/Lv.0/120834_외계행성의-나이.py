def solution(age):
    answer = ''
    str_age = str(age)
    
    for i in range(len(str_age)) :
        int_age = int(str_age[i])
        answer += chr(int_age + 97)

    return answer
