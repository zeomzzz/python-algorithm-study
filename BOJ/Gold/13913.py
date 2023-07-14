from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
check = [0] * 100001
# 경로 추적 : nxt를 기록하는 방식
def move(cur):
    data = []
    temp = cur

    for _ in range(visited[cur]+1):
        data.append(temp)
        temp = check[temp]

    print(' '.join(map(str, data[::-1])))

def bfs():
    q = deque()
    q.append(n)
    while q:
        cur = q.popleft()
        if cur == k:
            print(visited[cur])
            move(cur)
            return

        for nxt in (cur-1, cur+1, cur*2):
            if  0 <= nxt < 100001 and visited[nxt] == 0:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
                check[nxt] = cur

bfs()
