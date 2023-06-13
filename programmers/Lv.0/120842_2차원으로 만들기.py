def solution(num_list, n):
    answer = []
    
    for i in range(int(len(num_list)/n)) :
        tmp_list = []
        for j in range(n) :
            tmp_list.append(num_list[i*n + j])
        answer.append(tmp_list)
        
    return answer 
