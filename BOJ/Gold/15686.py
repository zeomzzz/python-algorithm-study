# 풀이 1
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())  # 도시 크기 N * N , 치킨집 최대 M개

city = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 치킨집, 집 담기
chickens = []
houses = []

for r in range(N) :
    for c in range(N) :
        if city[r][c] == 1 : # 집
            houses.append([r, c])
        elif city[r][c] == 2 : # 치킨집
            chickens.append([r, c])
            city[r][c] = 0 # 남길 치킨집만 표시하기 위해서 초기화

c = len(chickens) # 치킨집 개수 c
h = len(houses)

def distance(hr, hc) :
    res = 1e9

    for i in range(len(left)) : # 남긴 치킨집 중
        res = min(res, abs(left[i][0] - hr) + abs(left[i][1] - hc)) # 가장 가까운 거리 찾기

    return res


# 남길 치킨집 고르기
ans = 1e9
left = []
visited = [0] * c
def backtracking(idx, depth) :

    global c, visited, ans, d
    res = 0

    # base
    if depth == M :
        for i in range(h) :
            res += distance(houses[i][0], houses[i][1])
        ans = min(ans, res)
        return

    if idx == c :
        return

    # recursive
    for i in range(idx, c) :
        if not visited[i] : # i번째 방문 안했으면
            xr, xc = chickens[i][0], chickens[i][1]
            city[xr][xc] = 2 # 치킨집 남겨
            left.append([xr, xc])
            visited[i] = 1

            # 다음 고르러 ㄱㄱ
            backtracking(i + 1, depth + 1)

            # 원복
            city[xr][xc] = 0
            visited[i] = 0
            left.pop()

backtracking(0, 0)

print(ans)



# 풀이 2 : itertools combination 이용
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())  # 도시 크기 N * N , 치킨집 최대 M개

city = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 치킨집, 집 담기
chickens = []
houses = []

for r in range(N) :
    for c in range(N) :
        if city[r][c] == 1 : # 집
            houses.append((r, c))
        elif city[r][c] == 2 : # 치킨집
            chickens.append((r, c))

c = len(chickens) # 치킨집 개수 c
h = len(houses)

def distance(hr, hc) :
    res = 1e9

    for i in range(len(left)) : # 남긴 치킨집 중
        lr, lc = left[i]
        res = min(res, abs(lr - hr) + abs(lc - hc)) # 가장 가까운 거리 찾기

    return res


# 남길 치킨집 고르기
ans = 1e9

for j in range(1, M + 1) :
    for combi in combinations(chickens, j) : # 치킨집을 1개 ~ M개 고름
        left = list(combi)

        tmp = 0
        # 치킨 거리 구하자
        for i in range(h) :
            hr, hc = houses[i]
            tmp += distance(hr, hc)
            if tmp > ans : break

        ans = min(tmp, ans)

print(ans)
