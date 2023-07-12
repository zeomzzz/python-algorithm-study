import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input().rstrip())

# pq에 담기 : [원 좌표, 원 인덱스] : 좌표 순으로 정렬
# 하나씩 옮기면서 스택 짝 맞추기

pq = PriorityQueue()

for i in range(N) :
    x, r = map(int, input().rstrip().split()) # 중심 x좌표, 반지름 r
    pq.put((x - r, i))
    pq.put((x + r, i))

stack = []
while pq.qsize() != 0 :
    stack.append(pq.get())

    while len(stack) :
        x, idx = stack.pop()

        if len(stack) and stack[-1][1] == idx :
            stack.pop()
        else :
            stack.append((x, idx))
            break

if len(stack) : print("NO")
else : print("YES")
