def solution(keymap, targets):
    answer = []
    dict = {}
    
    for key in keymap :
        for i in range(len(key)) :
            if key[i] in dict : dict[key[i]] = min(dict[key[i]], i + 1)
            else : dict[key[i]] = i + 1
    
    for target in targets : 
        tmp = 0
        for i in range(len(target)) :
            if target[i] in dict : 
                tmp += dict[target[i]]
            else : 
                tmp = -1
                break
        answer.append(tmp)
        
    return answer
