from collections import deque

def solution(numbers, target):
    answer = 0
    
    # 1. 첫 줄은 양수, 둘째 줄은 음수인 그래프를 만든다
    numbers.insert(0, 0) # (0, 0)에서 출발하려고 insert
    l = len(numbers)
    graph = [numbers]
    tmp_numbers = []
    
    for i in range(len(numbers)) : tmp_numbers.append(numbers[i] * (-1))
    graph.append(tmp_numbers)
    
    q = deque()
    q.append((0, 0, 0))
    
    dr = [0, 1]

    while q :
        cr, cc, res = q.popleft()

        for i in range(2) :
            nr, nc = dr[i], cc + 1
            
            if nc == l : 
                if res == target : answer += 1
                break
            
            else :
                res += graph[nr][nc]
                q.append((nr, nc, res))
                res -= graph[nr][nc]
    
    return answer
