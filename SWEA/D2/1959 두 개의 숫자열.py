T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M :
        N, M = M, N
        A, B = B, A

    A += [0] * (M - N)

    sumLst = []
    cnt = 0
    while cnt < (M - N + 1) :
        sum = 0
        for i in range(M) :
            sum += A[i] * B[i]
        sumLst.append(sum)
        A = [0] + A[:-1]
        cnt += 1
    print(f'#{_ + 1} {max(sumLst)}')
