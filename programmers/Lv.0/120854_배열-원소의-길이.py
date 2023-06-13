def solution(strlist):
    answer = []
    i = 0
    for i in range(0, len(strlist)) :
        answer.append(len(strlist[i]))
        i += 1
    return answer
