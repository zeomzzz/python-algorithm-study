def solution(numbers):
    list = []
    answer = 0
    for i in range(0, len(numbers)) :
        for j in range(0, len(numbers)) :
            if i != j :
                list.append(numbers[i]*numbers[j])
            else :
                continue
    answer = max(list)
    return answer
