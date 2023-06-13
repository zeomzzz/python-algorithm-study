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
