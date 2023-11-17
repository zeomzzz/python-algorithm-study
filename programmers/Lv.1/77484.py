def solution(lottos, win_nums):
    answer = []
    same = 0
    zero = 0
    
    for lotto in lottos :
        if lotto in win_nums :
            same += 1
        elif lotto == 0 :
            zero += 1
    
    answer.append(find_rank(same + zero))
    answer.append(find_rank(same))
    
    return answer

def find_rank(num) :
    if num == 6 :
        return 1
    elif num == 5 :
        return 2
    elif num == 4 :
        return 3
    elif num == 3 :
        return 4
    elif num == 4 :
        return 5
    else :
        return 6
