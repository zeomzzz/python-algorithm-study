import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip()) # N : 일의 수

heap = []
for _ in range(N) :
    t, s = map(int, input().rstrip().split())
    # t시간, s 시 내에 끝내기
    # -> s-1시에는 마지막으로 하고 있어야 함
    # -> s-t시에는 시작해야 함
    heapq.heappush(heap, (s * (-1), t))

s, t = heapq.heappop(heap)
s = s * (-1)
start = s - t

flag = True
while heap and flag :
    s, t = heapq.heappop(heap)
    s = s * (-1)

    if start >= s :
        start = s - t
    else : # start < s
        start -= t

    if start < 0 :
        flag = False

if not flag : print(-1)
else : print(start)
