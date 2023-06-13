def solution(lines):
    answer = 0
    lines_ad = lines + [lines[0]]
    
    for i in range(0, 3) :
        a = max(lines_ad[i][0], lines_ad[i + 1][0])
        b = min(lines_ad[i][1], lines_ad[i + 1][1])
    
        if a < b :
            answer += b - a
    
    c = max(lines[0][0], lines[1][0], lines[2][0])
    d = min(lines[0][1], lines[1][1], lines[2][1])

    if c < d :
        answer -= (d - c) * 2

    return answer
