from collections import deque
import sys, heapq
input = sys.stdin.readline

n = int(input())
ans = 0
pq = []

times = [] # 시간표 전체
for _ in range(n) :
    times.append(list(map(int, input().split()))) # [시작, 종료]
times.sort() # 시작으로 정렬 -> 종료로 정렬
q = deque(times)

heapq.heappush(pq, q.popleft()[1]) # 종료시각을 넣고

while q :
    s, t = q.popleft() # 다음 강의 정보 꺼내기

    if s >= pq[0] : # 강의실 수업이 끝나고 시작하면
        heapq.heappop(pq) # 강의실 비우고
        heapq.heappush(pq, t) # 다음 강의 끝나는 시간 넣기
    else : # 수업 안끝났는데 시작하면
        heapq.heappush(pq, t) # 새로운 강의실에 수업 넣기

    if ans < len(pq) : ans = len(pq)

print(ans)
