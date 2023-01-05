T = int(input())

for i in range(T) :
    P, Q, R, S, W = map(int, input().split())

    # A사 요금
    costA = P * W

    # B사 요금
    if W < R :
        costB = Q
    else :
        costB = Q + (W - R) * S
    
    print(f'#{i + 1} {min(costA, costB)}')
