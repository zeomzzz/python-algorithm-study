import sys
input = sys.stdin.readline

left = list(input().rstrip()) # 처음에 위치가 맨 뒤, 즉 문자열이 다 왼쪽에
right = []
M = int(input().rstrip())  # 명령문의 개수 M
# right는 append, pop 사용하기 위해 역순!!

for _ in range(M) :
    cmd = input().rstrip().split()

    if cmd[0] == 'L' :
        if left : # 맨 앞 아니면
            right.append(left.pop())
    elif cmd[0] == 'D' :
        if right : # 맨 뒤 아니면
            left.append(right.pop())
    elif cmd[0] == 'B' :
        if left : # 맨 앞 아니면
            left.pop()
    elif cmd[0] == 'P' :
        left.append(cmd[1])

print("".join(left), end="")
print("".join(reversed(right)))
