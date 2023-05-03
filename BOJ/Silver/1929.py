import sys
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())

lst = [1] * (N + 1)
lst[0] = 0
lst[1] = 0

for i in range(2, N + 1) :
    if lst[i] :
        tmp = 2
        while True :
            idx = i * tmp

            if idx > N : break

            lst[idx] = 0
            tmp += 1

for i in range(M, N + 1) :
    if lst[i] : print(i)
