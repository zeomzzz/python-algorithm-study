def solution(t, p):
    answer = 0
    tl = len(t)
    pl = len(p)
    pint = int(p)
    
    # sliding window
    number = int(t[:pl])
    if number <= pint : answer += 1
    
    for i in range(pl, tl) :
        number = (number - (int(t[i - pl]) * (10 ** (pl - 1)))) * 10 + int(t[i])
        if number <= pint : answer += 1
    
    return answer
