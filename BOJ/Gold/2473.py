import sys
input = sys.stdin.readline

N = int(input().rstrip())
liquids = list(map(int, input().rstrip().split()))

liquids.sort()

mixed = abs(liquids[0] + liquids[1] + liquids[-1])
ans = [liquids[0], liquids[1], liquids[-1]]

# 맨 앞에 하나 고정하고 나머지를 투포인터 탐색
for i in range(N - 2) :
    fixed = i

    start = i + 1
    end = N - 1

    while start < end :

        tmpMixed = liquids[fixed] + liquids[start] + liquids[end]

        # 갱신할 수 있으면 갱신
        if mixed > abs(tmpMixed) :
            mixed = abs(tmpMixed)
            ans = [liquids[fixed], liquids[start], liquids[end]]

        # 포인터 이동
        if tmpMixed > 0 : end -= 1
        elif tmpMixed < 0 : start += 1
        else : break

print(*ans)
