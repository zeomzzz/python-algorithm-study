def solution(array):
    answer = 0
    for i in range(0, len(array)) :
        a = str(array[i])
        for j in range(0, len(a)) :
            if a[j] == "7" :
                answer += 1
    return answer
