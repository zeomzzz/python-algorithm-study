def solution(n, numlist):
    answer = []
    for i in range(len(numlist)) :
        if numlist[i]/n == int(numlist[i]/n) :
            answer.append(numlist[i])
    return answer
