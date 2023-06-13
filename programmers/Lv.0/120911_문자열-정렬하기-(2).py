def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    listed = list(my_string)
    listed.sort()
    
    i = 0
    while True :
        answer += listed[i]
        i += 1
        if i == len(my_string) :
            break
        
    return answer
