T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) > len(B) :
        A, B = B, A

    A = A + [0] * (len(B) - len(A))

    sumLst = []
    cnt = 0
    while cnt < ((abs(N - M)) + 1) :
        sum = 0
        for i in range(len(A)) :
            sum += A[i] * B[i]
        sumLst.append(sum)
        A = [0] + A[:-1]
        cnt += 1
    print(f'#{_ + 1} {max(sumLst)}')
