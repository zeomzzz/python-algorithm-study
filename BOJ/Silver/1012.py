from collections import deque

t = int(input()) # tc 수

def bfs(a, b) :
  q = deque()
  q.append([a, b])
  land[a][b] = 0

  while q :
    a, b = q.popleft()

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(4) :
      nr = a + dr[i]
      nc = b + dc[i]

      if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1 :
        land[nr][nc] = 0
        q.append([nr, nc])

for _ in range(t) :
  m, n, k = map(int, input().split()) # 가로 m, 세로 n, 배추 위치의 개수 k

  land = [[0] * m for _ in range(n)] # 배추 위치 입력
  for i in range(k) :
    a, b = map(int, input().split())
    land[b][a] = 1
  
  cnt = 0

  for i in range(n) :
    for j in range(m) :
      if land[i][j] == 1 :
        bfs(i, j)
        cnt += 1 # bfs 한세트 = 하나의 배추흰지렁이가 보호할 수 있는 범위

  print(cnt)
