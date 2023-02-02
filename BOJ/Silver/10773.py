import sys

T = int(sys.stdin.readline())

stack = []

for _ in range(T) :
  n = int(sys.stdin.readline())

  # 0을 부르지 않았으면 stack에 추가, 0을 불렀으면 stack 마지막 요소를 제거(pop)
  if n != 0 :
    stack.append(n)
  else :
    stack.pop()

print(sum(stack))
