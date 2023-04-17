import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, k = map(int, input().split()) # 친구 1~N, 친구관계 M개, 비용 제한 k
A = list(map(int, input().split()))
A.insert(0, 0)

p = [i for i in range(N + 1)] # 학생 1 ~ N

def findSet(x) :
    if x != p[x] :
        p[x] = findSet(p[x])
    return p[x]

for _ in range(M) :
    v, w = map(int, input().split())

    if A[findSet(v)] < A[findSet(w)] : #v의 친구비가 더 적으면 v를 대표자로
        p[findSet(w)] = findSet(v)
    else :
        p[findSet(v)] = findSet(w)

for i in range(1, N + 1) : # 대표자 업데이트
    p[i] = findSet(i)

distinct_p = list(set(p[1:])) # 대표자를 중복되지 않게 저장
price = 0
for p in distinct_p :
    price += A[p]

if price > k :
    print("Oh no")
else :
    print(price)
