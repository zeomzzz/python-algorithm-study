from collections import deque

t = int(input()) # tc 개수

def bfs(cr, cc, gr, gc) :
  # 출발 = 도착 같으면 0
  if cr == gr and cc == gc :return 0

  q = deque()
  q.append([cr, cc])
  chess[cr][cc] = 1

  while q :
    r, c = q.popleft()

    dr = [-1, -1, 1, 1, -2, -2, 2, 2]
    dc = [2, -2, 2, -2, 1, -1, 1, -1]

    for i in range(8) :
      nr = r + dr[i]
      nc = c + dc[i]

      if 0 <= nr < l and 0 <= nc < l and chess[nr][nc] == 0 :
        chess[nr][nc] = chess[r][c] + 1
        q.append([nr, nc])

        if nr == gr and nc == gc :
          return chess[gr][gc] - 1

for _ in range(t) :
  l = int(input()) # 체스판 한 변의 길이
  cr, cc = map(int, input().split()) # current
  gr, gc = map(int, input().split()) # goal

  chess = [[0] * l for _ in range(l)]

  print(bfs(cr, cc, gr, gc))
