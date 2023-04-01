import sys, heapq
input = sys.stdin.readline

heap = []

n = int(input()) # 연산의 개수 n
for _ in range(n) :
    x = int(input())
    if x != 0 :
        heapq.heappush(heap, x * (-1))
    else :
        if len(heap) != 0 :
            tmp = heapq.heappop(heap)
            print(tmp * (-1))
        else :
            print(0)
