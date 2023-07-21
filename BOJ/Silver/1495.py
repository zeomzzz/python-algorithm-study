import sys
from collections import deque
input = sys.stdin.readline

N, S, M = map(int, input().rstrip().split()) # 곡의 개수 N, 시작 볼륨 S, 볼륨 max M
V = list(map(int, input().rstrip().split()))
V.insert(0, 0)

dp = [[False] * (M + 1) for _ in range(N + 1)]
# [r][c] : r번째에 c 볼륨

q = deque()
q.append((0, S))
dp[0][S] = True

dc = [1, -1]

while q :

    cr, cc = q.popleft() # 현재 cr 번째 곡, 볼륨 cc

    for i in range(2) :
        nr = cr + 1

        if nr < N + 1 and 0 <= cc + V[nr] * dc[i] < M + 1 :
            nc = cc + V[nr] * dc[i]
            if dp[nr][nc] == False :
                dp[nr][nc] = True
                q.append((nr, nc))

ans = -1
for i in range(M, -1, -1) :
    if dp[N][i] == True :
        ans = i
        break

print(ans)
