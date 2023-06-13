def solution(s):
    answer = 0
    i = 0
    
    s_split = s.split(" ")
    
    while True :
        if i == len(s_split) - 1 :
            break
        elif s_split[i + 1] == "Z" :
            del s_split[i + 1]
            del s_split[i]
            i -= 1  # list 요소 삭제로 인한 인덱스 변동 고려
        else :
            i += 1
    
    for j in s_split :
        answer += int(j)
    
    return answer
