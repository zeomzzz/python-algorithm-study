import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

NGF = [-1] * N
stack = [0] # NGF를 구해야하는 A의 인덱스 담음

F = {} # 등장횟수 넣는 dictionary
for a in A :
    if str(a) in F : F[str(a)] += 1
    else : F[str(a)] = 1 # dict에 a 없으면 초기 세팅

for i in range(1, N) :
    while stack and F[str(A[stack[-1]])] < F[str(A[i])] :
        NGF[stack[-1]] = A[i]
        stack.pop()

    stack.append(i)

print(*NGF)
