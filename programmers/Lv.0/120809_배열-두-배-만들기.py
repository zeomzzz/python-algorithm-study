def solution(numbers):
    answer = []
    for i in range(0, len(numbers)) :
        num2 = numbers[i] * 2
        answer.append(num2)
        i += 1
    return answer
