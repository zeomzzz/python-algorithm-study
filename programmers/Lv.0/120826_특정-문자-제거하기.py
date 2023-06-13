def solution(my_string, letter):
    answer = ''
    for i in range(0, len(my_string)) :
#my_string이 바뀌어서 인덱스 혼동되지 않도록 answer에 추가  
        if my_string[i] != letter :
            answer += my_string[i]
    return answer
