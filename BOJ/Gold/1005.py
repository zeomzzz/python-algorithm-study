from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t) :
    n, k = map(int, input().rstrip().split()) # 건물의 개수 n, 규칙의 총 개수 k
    times = list(map(int, input().split()))
    times.insert(0, 0)

    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    starts = set(range(1, n + 1))
    q = deque()
    dp = [0] * (n + 1)
    stack = []

    for _ in range(k) :
        x, y = map(int, input().split())  # x -> y
        adj[x].append(y)
        indegree[y] += 1
        starts.discard(y)
    starts = list(starts)

    w = int(input()) # 백준이가 지어야 할 건물
    # 입력 끝

    for s in starts :
        q.append(s)
        dp[s] = times[s]

    while q :
        cur = q.popleft()
        stack.append(cur)

        if cur == w : break

        for nxt in adj[cur] : # 선행조건 다 해서 수행할 수 있는 상태
            indegree[nxt] -= 1

            if indegree[nxt] == 0 :
                q.append(nxt)
    stack.insert(0, 0)

    for i in range(1, len(stack)) :
        if dp[stack[i]] == 0 :

            for j in range(i - 1, 0, -1) :
                if stack[i] in adj[stack[j]] : # stack[i]가 stack[j] 다음이면
                    dp[stack[i]] = max(dp[stack[i]], dp[stack[j]] + times[stack[i]])

    print(dp[w])
