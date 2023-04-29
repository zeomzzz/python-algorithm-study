import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 수열 A 의 길이 N
A = list(map(int, input().rstrip().split())) # 수열 A
stack = []
NGE = [-1] * N

for i in range(N - 1, -1, -1) :
    while True :
        if not stack :
            stack.append(A.pop())
            break
        else :
            if stack[-1] > A[-1] :
                NGE[i] = stack[-1]
                stack.append(A.pop())
                break
            else :
                stack.pop()

print(*NGE)
