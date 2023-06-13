def solution(num_list):
    answer = []
    k = 0
    for i in range(0, len(num_list)) :
        if num_list[i] % 2 == 0 :
            k += 1
    j = len(num_list) - k
    answer.append(k)
    answer.append(j)
    return answer
