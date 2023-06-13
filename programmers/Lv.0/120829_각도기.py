def solution(angle):
    if 0 < angle < 90:
        answer = 1
        return answer
    elif angle == 90:
        answer = 2
        return answer
    elif 90 < angle < 180:
        answer = 3
        return answer
    else:
        answer = 4
    return answer
