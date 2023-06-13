def solution(keyinput, board):
    [a, b] = board
    x = 0
    y = 0
    
    for i in keyinput :
    
        if i == 'up' :
            if y + 1 <= b // 2 :
                y += 1
        elif i == 'down' :
            if y - 1 >= - ( b // 2 ) :
                y -= 1
        elif i == 'right' :
            if x + 1 <= a // 2 :
                x += 1
        elif i == 'left' :
            if x - 1 >= - ( a // 2 ) :
                x -= 1
    
    answer = [x, y]
    
    return answer
