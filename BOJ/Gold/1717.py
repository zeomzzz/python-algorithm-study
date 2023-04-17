import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split()) # 집합 0 ~ n, m : 연산의 개수
p = [i for i in range(n + 1)] # make-set

def findSet(x) :
    if x != p[x] :
        p[x] = findSet(p[x])
    return p[x]

for i in range(m) :
    x, a, b = map(int, input().split())

    if x == 0 :
        p[findSet(a)] = findSet(b) # union
    else :
        if findSet(a) == findSet(b) :
            print("YES")
        else :
            print("NO")
