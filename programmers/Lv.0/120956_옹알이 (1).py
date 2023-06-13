def solution(babbling):
    pronounce = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in range(len(babbling)) :
      
        # 1) 문자열에서 가능한 발음 공백으로 바꿈
        for j in pronounce :
            if j in babbling[i] :
                space = ' ' * len(j)
                babbling[i] = babbling[i].replace(j, space, 1)
        
        # 2) 공백 삭제
        babbling[i] = babbling[i].replace(' ', '')
        
        # 3) 발음할 수 있는 것 뺴고 남은 것이 없는 문자열(= 발음 가능) count
        if babbling[i] == '' :
            answer += 1
                
    return answer
