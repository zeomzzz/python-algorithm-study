def solution(numbers, direction):
    answer = []
    num_len = len(numbers)
    
    if direction == "right" :
        answer.append(numbers[num_len - 1])
        
        for i in range(0, num_len - 1) :
            answer.append(numbers[i])
    
    elif direction == "left" :
        for i in range(1, num_len) :
            answer.append(numbers[i])
        
        answer.append(numbers[0])
    
    return answer
