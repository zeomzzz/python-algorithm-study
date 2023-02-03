import sys

T = int(sys.stdin.readline().rstrip())
cnt = 0

for _ in range(T) :
  words = sys.stdin.readline().rstrip()
  stack = []

  for i in words :
    # 단어와 이전 단어 동일하면 pop
    # 이외의 경우에는 모두 stack에 저장
    if len(stack) > 0 :
      if i == stack[-1] :
        stack.pop()
      else :
        stack.append(i)
    else :
      stack.append(i)
  
  # 반복문 종료되었을 때 stack이 비워져야(짝이 맞으므로) -> 좋은 단어
  if len(stack) == 0 :
    cnt += 1

print(cnt)
