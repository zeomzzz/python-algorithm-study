def solution(before, after):
    answer = 0
    
    list_before = list(before)
    list_after = list(after)
    
    list_before.sort()
    list_after.sort()
    
    if list_before == list_after :
        answer += 1
    
    return answer
