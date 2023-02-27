import sys

n = int(sys.stdin.readline().rstrip())
ans = []

def move(n, a, b, c) : # a, b, c : 원판 번호

    if n == 1 :
        print(a, c) # 가장 큰 원판 1번 위치에서 3번으로

    else :
        move(n-1, a, c, b) # 원판 번호 중 2, 3을 바꿈 (마지막 원판 빼고 2로 옮긺)
        print(a, c)
        move(n-1, b, a, c) # 원판 번호 중 1, 2를 바꿈 (2번 자리가 1번 자리 역할)

cnt = 2 ** n - 1

print(cnt)
move(n, 1, 2, 3)
