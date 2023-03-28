import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
min_cost = 0

def perm(idx, visited, cost, cur) :
    global min_cost

    # base
    if min_cost != 0 :
        if cost > min_cost :
            return

    if idx == n :
        if w[cur][0] > 0 :
            cost += w[cur][0] # 마지막에 0으로 다시 돌아옴
            if min_cost != 0 : min_cost = min(min_cost, cost)
            else : min_cost = cost
            return
        else : return

    # recursive
    for i in range(1, n) :
        if (visited & (1 << i)) == 0 and w[cur][i] > 0 : # i 안 썼고 비용 0 초과이면
            perm(idx + 1, visited | (1 << i), cost + w[cur][i], i)

perm(1, 0, 0, 0)

print(min_cost)
