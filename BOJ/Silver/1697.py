from collections import deque

n, k = map(int, input().split()) # n : 수빈 위치, k : 동생 위치

visited = [0] * 100001

def bfs(v, target) :
  if v == target : return 0

  q = deque()
  q.append(v)
  visited[v] = 1

  while q :
    x = q.popleft()

    dx = [-1, 1, x] # a : x일 때 순간이동하면 2*x 이므로
    
    for i in range(3) :
      nx = x + dx[i]

      if 0 <= nx <= 100000 and visited[nx] == 0 :
        visited[nx] = visited[x] + 1
        q.append(nx)

        if nx == target :
          return visited[nx] - 1 # 출발 지점에서 visited = 1로 시작해서

print(bfs(n, k))
