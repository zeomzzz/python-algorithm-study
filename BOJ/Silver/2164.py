import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

# cards에 카드 번호 입력 (맨 앞이 맨 위의 카드)
cards = deque(range(1, N+1))

cnt = 0

# 마지막 카드만 남을 때까지 반복
while len(cards) > 1:
  if cnt % 2 == 0 :
    cards.popleft()
  else :
    cards.append(cards.popleft())
  cnt += 1

print(cards[0])
