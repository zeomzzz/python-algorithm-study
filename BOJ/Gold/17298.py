import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 수열 A 의 길이 N
A = list(map(int, input().rstrip().split())) # 수열 A
stack = []
NGE = [-1] * N

for i in range(N - 1, -1, -1) :
    while stack and stack[-1] <= A[-1] :
        stack.pop()

    if stack : NGE[i] = stack[-1]
    stack.append(A.pop())

print(*NGE)
