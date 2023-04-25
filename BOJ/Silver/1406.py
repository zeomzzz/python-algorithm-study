import sys
input = sys.stdin.readline

stack = list(input().rstrip()) # 처음에 위치가 맨 뒤, 즉 문자열이 다 왼쪽에
lst = []
M = int(input().rstrip())  # 명령문의 개수 M
# stack이 커서의 왼쪽, lst가 커서의 오른쪽 (lst는 append, pop 사용하기 위해 역순!!)

for _ in range(M) :
    cmd = input().rstrip().split()

    if cmd[0] == 'L' :
        if len(stack) : # 맨 앞 아니면
            lst.append(stack.pop())
    elif cmd[0] == 'D' :
        if len(lst) : # 맨 뒤 아니면
            stack.append(lst.pop())
    elif cmd[0] == 'B' :
        if len(stack) : # 맨 앞 아니면
            stack.pop()
    elif cmd[0] == 'P' :
        stack.append(cmd[1])

lst = lst[::-1]
for s in stack : print(s, end="")
for l in lst : print(l, end="")
