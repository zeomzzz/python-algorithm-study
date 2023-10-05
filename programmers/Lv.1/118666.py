def solution(survey, choices):
    global score
    
    answer = ''
    score = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(survey)) : calculate(survey[i], choices[i])
    
    if score["R"] >= score["T"] : answer += "R"
    else : answer += "T"
    
    if score["C"] >= score["F"] : answer += "C"
    else : answer += "F"
    
    if score["J"] >= score["M"] : answer += "J"
    else : answer += "M"
    
    if score["A"] >= score["N"] : answer += "A"
    else : answer += "N"
    
    return answer

def calculate(question, choice) :
    global score
    
    if choice == 4 : return
    elif choice > 4 :
        score[question[0]] -= choice - 4
        return
    else :
        score[question[1]] += choice - 4
        return
