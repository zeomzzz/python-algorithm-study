def solution(quiz):
    answer = []
    
    for i in quiz : 
        quiz_split = i.split(' ')
        if quiz_split[1] == '+' :
            if int(quiz_split[0]) + int(quiz_split[2]) == int(quiz_split[4]) :
                answer.append('O')
            else :
                answer.append('X')
        else :
            if int(quiz_split[0]) - int(quiz_split[2]) == int(quiz_split[4]) :
                answer.append('O')
            else :
                answer.append('X')
    
    return answer
