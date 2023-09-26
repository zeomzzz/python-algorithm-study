from collections import deque

def solution(places):
    answer = []
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    for place in places :
        flag = True # 거리두기 지킴
        for r in range(5) :
            if not flag : break
            for c in range(5) :
                if not flag : break
                if place[r][c] == "P" : # bfs로 확인
                    visited = [[-1] * 5 for _ in range(5)]
                    
                    q = deque()
                    q.append((r, c))
                    visited[r][c] = 0
                    
                    while q and flag :
                        cr, cc = q.popleft()
                        
                        if visited[cr][cc] < 2 :
                            for i in range(4) :
                                nr, nc = cr + dr[i], cc + dc[i]

                                if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] == -1 :
                                    visited[nr][nc] = visited[cr][cc] + 1

                                    if place[nr][nc] == "X" : pass
                                    elif place[nr][nc] == "O" : q.append((nr, nc))
                                    else : 
                                        flag = False
                                        break
                                        
        if flag : answer.append(1)
        else : answer.append(0)
    
    return answer
