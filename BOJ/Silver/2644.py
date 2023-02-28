from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)] # 촌수 표시하는 그래프
visited = [0] * (n + 1)

# graph에 부모자식 관계 입력
for _ in range(m) :
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

def bfs(v, target) :
  q = deque()
  q.append(v)
  
  visited[v] = 1

  while q :
    a = q.popleft()

    for i in range(1, n + 1) :
      if visited[i] == 0 and graph[i][a] : # i 방문 안했고 a랑 부모-자식 관계이면
          q.append(i)
          visited[i] = visited[a] + 1
          
          if i == target :
            return visited[i] - 1

  return -1

print(bfs(p1, p2))
