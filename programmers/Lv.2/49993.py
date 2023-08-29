def solution(skill, skill_trees):
    answer = 0
    
    skill = list(skill)
    
    for skill_tree in skill_trees :
        idx = 0 # skill의 index
        flag = True
            
        for i in range(len(skill_tree)) :
            if skill_tree[i] in skill :
                if skill_tree[i] == skill[idx] :
                    idx += 1 # 다음 skill 배우러
                    if idx == len(skill) : break # 모든 skill 다 배웠으므로 종료
                else :
                    flag = False
                    break
                        
        if flag : answer += 1
    
    return answer
