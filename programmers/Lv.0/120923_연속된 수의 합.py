def solution(num, total):
    answer = []
    
    i = (total - (num * (num - 1)) / 2) / num
    
    while len(answer) < num :
        answer.append(i)
        i += 1
    
    return answer
