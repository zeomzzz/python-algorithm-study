import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 기차의 수 N, 명령의 수 M
trains = [0 for _ in range(N + 1)]

for _ in range(M) :
    orders = list(map(int, input().rstrip().split()))

    match orders[0] :
        case 1 :
            i, x = orders[1], orders[2]
            trains[i] = trains[i] | (1 << (x - 1))
        case 2 :
            i, x = orders[1], orders[2]
            trains[i] = trains[i] & (~(1 << (x - 1)))
        case 3 :
            i = orders[1]
            trains[i] = (trains[i] & (~(1 << 19))) << 1
        case 4 :
            i = orders[1]
            trains[i] = trains[i] >> 1

print(len(set(trains[1:])))
