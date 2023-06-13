def solution(my_string):
    
    # 띄어쓰기 기준으로 split
    split_list = my_string.split(' ')
    answer = int(split_list[0])
    
    # 짝수 인덱스는 정수, 홀수 인덱스는 연산자임을 이용
    for i in range(0, int(len(split_list) // 2)) :
        if split_list[2 * i + 1] == '+' :
            answer += int(split_list[2 * i + 2])
        else :
            answer -= int(split_list[2 * i + 2])
    
    return answer
