import sys
input = sys.stdin.readline

N = int(input()) # 도시의 수 N
M = int(input()) # 여행계획에 속한 도시들의 수 M
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
ans = "YES"

def FindSet(x) :
    if x != p[x] :
        p[x] = FindSet(p[x])
    return p[x]

# make-set
p = [i for i in range(N)]  # 도시 번호 0 ~ N - 1

# 1이면 연결
for r in range(N) :
    for c in range(N) :
        if graph[r][c] == 1 and FindSet(r) != FindSet(c) : # 연결되어있고, 현재 연결되어있지 않으면
            p[FindSet(r)] = FindSet(c) # Union

for i in range(M - 1) :
    if FindSet(plan[i] - 1) != FindSet(plan[i + 1] - 1) : # 문제는 1 ~ N인데 코드는 0 ~ N - 1
        ans = "NO"
        break

print(ans)
