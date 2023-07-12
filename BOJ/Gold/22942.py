# 우큐 정렬하고 스택 짝 맞추기
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


# 왼쪽 x좌표로 정렬 후 원 두 개 씩 비교
import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input().rstrip())

# o1left o2left o2right o1right

circles = []

for _ in range(N) :
    x, r = map(int, input().rstrip().split())
    circles.append([x - r, x + r])

circles.sort()

ans = True

for i in range(N - 1) :
    o1_left, o1_right = circles[i][0], circles[i][1]
    o2_left, o2_right = circles[i + 1][0], circles[i + 1][1]

    if o1_left == o2_left or o1_right == o2_right or o2_left < o1_right < o2_right :
        ans = False
        break

if ans : print("YES")
else : print("NO")
