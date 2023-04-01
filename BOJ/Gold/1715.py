import sys, heapq
input = sys.stdin.readline

n = int(input())

heap = []
cnt = 0

for _ in range(n) :
    heapq.heappush(heap, int(input()))

while len(heap) > 2 :

    tmp = heapq.heappop(heap) + heapq.heappop(heap)
    cnt += tmp
    heapq.heappush(heap, tmp)

if len(heap) > 1 :
    cnt += heap[0] + heap[1]

print(cnt)
