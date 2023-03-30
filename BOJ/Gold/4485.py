import heapq
import sys
input = sys.stdin.readline

tc = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def djk(r, c) :
    global dist

    q = []
    heapq.heappush(q, (cave[r][c], r, c))
    dist[r][c] = 0

    while q :
        cost, cr, cc = heapq.heappop(q)

        if cr == n - 1 and cc == n - 1 :
            break

        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < n and 0 <= nc < n :
                ncost = cost + cave[nr][nc]

                if ncost < dist[nr][nc] :
                    dist[nr][nc] = ncost
                    heapq.heappush(q, (ncost, nr, nc))

t = 1

while True :
    n = int(input())

    if n == 0 : break

    cave = [list(map(int, input().split())) for _ in range(n)]
    dist = [[sys.maxsize] * n for _ in range(n)] # rupee max 이상으로 초기화

    djk(0, 0)

    print("Problem " + str(t) + ": " + str(dist[n - 1][n - 1]))

    t += 1
