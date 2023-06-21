import sys
from collections import deque
input = sys.stdin.readline

# 번호표 순서대로만 통과할 수 있는 입구
# 콘서트장으로 입장할 수도 있고 대기 공간에서 다시 기다릴 수도

N = int(input().rstrip()) # N줄
lines = ''

for _ in range(N) :
    lines += input().rstrip() + " "

lines = lines.split()
lines_origin = []
for l in lines :
    tmp = l.split("-")
    tmp[1] = int(tmp[1])
    lines_origin.append(tmp)

lines_sorted = sorted(lines_origin, key=lambda x: (x[0], x[1]))

q = deque(lines_origin)
stack = []

# 줄 세운거랑 비교
isGood = True
idx = 0

while True :

    # 일단,, 지금 사람 확인
    if len(q) > 0 :
        cur = q.popleft()

    if idx < N and cur == lines_sorted[idx] :
        idx += 1

    else :

        if len(stack) > 0 and stack[-1] == lines_sorted[idx] :
            q.appendleft(cur)
            stack.pop()
            idx += 1
        else :
            stack.append(cur)

    if not q :
        break

if len(stack) > 0 :
    while True :
        cur = stack.pop()
        if cur == lines_sorted[idx] :
            idx += 1
        else :
            isGood = False
            break

        if len(stack) == 0 : break

if isGood : print("GOOD")
else : print("BAD")
