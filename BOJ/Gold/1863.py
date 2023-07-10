import sys

input = sys.stdin.readline

n = int(input().rstrip())
stack = []
cnt = 0

for i in range(n):
    x, y = map(int, input().rstrip().split())  # y가 높이

    while len(stack) > 0 and stack[-1] > y :
        cnt += 1
        stack.pop()
    
    if len(stack) > 0 and stack[-1] == y : continue # 같으면 스택에 안넣음
        
    stack.append(y)

# 남은 stack
while len(stack) > 0 :
    if stack[-1] > 0 : cnt += 1
    stack.pop()

print(cnt)
