import sys, heapq
input = sys.stdin.readline

heap = []

n = int(input()) # 연산의 개수 n
for _ in range(n) :
    x = int(input())
    if x != 0 :
        heapq.heappush(heap, x)
    else :
        if len(heap) != 0 :
            print(heapq.heappop(heap))
        else :
            print(0)
