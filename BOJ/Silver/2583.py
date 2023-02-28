from collections import deque

def bfs(a, b) :
  q = deque()
  q.append([a, b])
  visited[a][b] = 1
  area = 1 # 넓이

  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]

  while q :
    r, c = q.popleft()
    
    for i in range(4) :
      nr = r + dr[i]
      nc = c + dc[i]

      if 0 <= nr < m and 0 <= nc < n and square[nr][nc] == 0 and visited[nr][nc] == 0 : # 범위 안이고 + 방문 안했을 때
        visited[nr][nc] = 1
        q.append([nr, nc])
        area += 1

  return area

m, n, k = map(int, input().split()) # k개의 직사각형
square = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
area_lst = []

# k개의 사각형 칠하기
for _ in range(k) :
  c1, r1, c2, r2 = map(int, input().split())
  for r in range(r1, r2) :
    for c in range(c1, c2) :
      square[r][c] = 1

# print(square) v# 넓이 잘 칠함

cnt = 0
for r in range(m) :
  for c in range(n) :
    if square[r][c] == 0 and visited[r][c] == 0 :
      cnt += 1
      area_lst.append(bfs(r, c))

area_lst.sort()

print(cnt)
print(*area_lst)
