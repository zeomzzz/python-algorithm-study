def solution(num, k):
    answer = 0
    str_num = str(num)

    for i in range(0, len(str_num)) :

        if str_num[i] == str(k) :
            answer = i + 1
            break

    if answer == 0 :
        answer = -1

    return answer
