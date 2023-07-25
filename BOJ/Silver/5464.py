import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # N개의 주차 공간, M대의 차량

prices = []
for _ in range(N) : prices.append(int(input().rstrip())) # 무게당 요금
weights = [0]
for _ in range(M) : weights.append(int(input().rstrip())) # 차량(1~M)의 무게
parked = [0 for _ in range(M + 1)] # i번 차를 주차한 위치
income = 0

# 다음 차량이 들어갈 수 있는 자리를 우큐로 관리
pq = [i for i in range(N)]
tmp = []

for i in range(2 * M) :
    car = int(input().rstrip())

    if car > 0 :
        if pq :
            space = heapq.heappop(pq) # 주차할 수 있는 자리
            parked[car] = space
            income += weights[car] * prices[space]

        else :
            tmp.append(car)

    else :
        car *= (-1)
        space = parked[car]
        heapq.heappush(pq, space) # 주차 가능한 자리로 추가
        parked[car] = 0

        if tmp : # 주차 못했던 차 있으면 주차
            car = tmp.pop(0)
            space = heapq.heappop(pq)  # 주차할 수 있는 자리
            parked[car] = space
            income += weights[car] * prices[space]

print(income)
