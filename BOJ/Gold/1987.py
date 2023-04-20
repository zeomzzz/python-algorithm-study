import sys
input = sys.stdin.readline

R, C = map(int, input().split()) # 세로 R, 가로 C

graph = list(list(input().rstrip()) for _ in range(R))
lst = set()
for g in graph :
    lst.update(g)
# visited = [[0] * C for _ in range(R)]
alphabet = [0] * 26 # 알파벳 방문체크
max_depth = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(cr, cc, depth) : # 현재 r, 현재 c, 깊이
    global max_depth, dr, dc

    for i in range(4) :
        nr = cr + dr[i]
        nc = cc + dc[i]

        if 0 <= nr < R and 0 <= nc < C : # 범위 안에 있고
            na = graph[nr][nc] # 새로 가려는 곳의 알파벳
            if not alphabet[ord(na) - ord("A")] : # 방문 안했고 알파벳 안썼으면
                # visited[nr][nc] = True
                alphabet[ord(na) - ord("A")] = True
                max_depth = max(max_depth, depth + 1)

                if max_depth == len(lst) : break

                dfs(nr, nc, depth + 1)
                # visited[nr][nc] = False
                alphabet[ord(na) - ord("A")] = False

# visited[0][0] = 1
alphabet[ord(graph[0][0]) - ord("A")] = 1

dfs(0, 0, 1)

print(max_depth)
