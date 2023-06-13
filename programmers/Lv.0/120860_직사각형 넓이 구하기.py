def solution(dots):
    
    dots.sort(reverse = True)
    
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
    side_1 = ((x4 - x2) ** 2 + (y4 - y2) ** 2) ** (1/2)
    side_2 = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** (1/2)
    
    answer = side_1 * side_2
    
    return answer
