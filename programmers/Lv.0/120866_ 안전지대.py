# 3차(통과) : list 복제했을 때 각 요소의 id도 달라지도록 deepcopy 
def solution(board):
    import copy
    
    answer = 0
    padding = []
    
    while len(padding) < len(board) + 2 :
        padding.append(2)
    
    for i in board :
        i.insert(0, 2)
        i.append(2)
    
    board.insert(0, padding)
    board.append(padding)
    
    board_cp = copy.deepcopy(board)

    for j in range(1, len(board)-1) :
        for k in range(1, len(board)-1) :
            if board[j][k] == 1 :
                board_cp[j-1][k-1] = 2
                board_cp[j-1][k] = 2
                board_cp[j-1][k+1] = 2
                board_cp[j][k-1] = 2
                board_cp[j][k+1] = 2
                board_cp[j+1][k-1] = 2
                board_cp[j+1][k] = 2
                board_cp[j+1][k+1] = 2
    
    for l in board_cp :
        answer += l.count(0)

    return answer



# 1차 (정확성 63.0/100.0)
def solution(board):
    answer = 0
    
    for i in board :
        for j in range(len(board)) :
            if i[j] == 1 :
                if j-1 >= 0 and i[j-1] != 1 :
                    i[j-1] = 2
        for j in range(len(board)) :
            if i[j] == 1 :
                if j+1 < len(board) and i[j+1] != 1 :
                    i[j+1] = 2
    
    for k in range(len(board)) :
        if 1 in board[k] :
            if k-1 >= 0 :
                board[k-1] = board[k]
        if 1 in board[k] :
            if k+1 < len(board) :
                board[k+1] = board[k]
    
    for l in board :
        answer += l.count(0)
    
    return answer
  
 
# 2차 (정확성 : 79.6 / 100.0)
def solution(board):
    answer = 0
    padding = []
    
    while len(padding) < len(board) + 2 :
        padding.append(2)
    
    for i in board :
        i.insert(0, 2)
        i.append(2)
    
    board.insert(0, padding)
    board.append(padding)
    
    board_cp = board.copy()

    for j in range(2, len(board)) :
        for k in range(2, len(board)) :
            if board[j][k] == 1 :
                board_cp[j-1][k-1] = 2
                board_cp[j-1][k] = 2
                board_cp[j-1][k+1] = 2
                board_cp[j][k-1] = 2
                board_cp[j][k+1] = 2
                board_cp[j+1][k-1] = 2
                board_cp[j+1][k] = 2
                board_cp[j+1][k+1] = 2
    
    for l in board_cp :
        answer += l.count(0)

    return answer
