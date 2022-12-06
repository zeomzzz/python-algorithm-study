# 풀이 1

def solution(numbers):

    answer = [i + j for j in numbers for i in numbers]
    
    for k in numbers :
        if 2 * k in answer :
            answer.remove(2 * k)

    answer = sorted(list(set(answer)))
            
    return answer
 

# 풀이 2

def solution(numbers):
    answer = []
    len_num = len(numbers)
    
    for i in range(len_num) :
        for j in range(len_num) :
            if i < j :
                answer.append(numbers[i] + numbers[j])
    
    answer = sorted(list(set(answer)))
    
    return answer
