def solution(numlist, n):
    answer = []
    diff = 0
    
    numlist_max = max(numlist)
    numlist_min = min(numlist)
    
    max_diff = max([abs(n - numlist_max), abs(n - numlist_min)])
    
    numlist_sorted = sorted(numlist, reverse = True)
    
    while diff <= max_diff :
        for i in numlist_sorted :
            if abs(i - n) == diff :
                answer.append(i)
        diff += 1
    
    return answer
