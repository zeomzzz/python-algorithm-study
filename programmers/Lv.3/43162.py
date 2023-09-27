from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    
    for i in range(n) :
        if visited[i] == 0 : # i번째 컴퓨터 아직 확인 안했다면
            
            answer += 1
            
            q = deque()
            q.append(i)
            visited[i] = 1
            
            while q :
                cur = q.popleft()
                
                for nxt in range(n) :
                    if not visited[nxt] and computers[cur][nxt] == 1 : # nxt에 방문하지 않았고 연결되어있으면
                        q.append(nxt)
                        visited[nxt] = 1
            
    return answer
