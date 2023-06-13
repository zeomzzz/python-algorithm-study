def solution(spell, dic):

    for i in dic :
        for j in spell :
            if j not in i :
                answer = 2
                break
            answer = 1
        if answer == 1 :
            break
        
    return answer
