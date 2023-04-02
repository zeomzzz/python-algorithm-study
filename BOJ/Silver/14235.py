import sys, heapq
input = sys.stdin.readline

n = int(input()) # 총 방문 횟수 n

pq = []

for _ in range(n) :
    tmp = list(map(int, input().split()))
    a = tmp[0]

    if a == 0 : # 아이들 만남
        if len(pq) == 0 : print(-1)  # 줄 선물이 없음
        else : print(heapq.heappop(pq) * (-1)) # 줄 선물 있음
    else :
        # tmp[0] : 선물 개수
        for i in range(1, a + 1) :
            heapq.heappush(pq, tmp[i] * (-1))
