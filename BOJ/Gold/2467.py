import sys
input = sys.stdin.readline

N = int(input().rstrip())
liquids = list(map(int, input().rstrip().split()))

# 오름차순 정렬
# 두 개의 합이 0 초과 -> 오른쪽 포인터를 왼쪽으로 한 칸
# 두 개의 합이 0 미만 -> 왼쪽 포인터를 오른쪽으로 한 칸
# 0 이면 종료

liquids.sort()

# 투 포인터
left = 0
right = N - 1

minSum = abs(liquids[right] + liquids[left])
ans = [liquids[left], liquids[right]]

while left < right :
    liqSum = liquids[left] + liquids[right]

    if minSum > abs(liqSum):
        minSum = abs(liqSum)
        ans = [liquids[left], liquids[right]]

    if liqSum > 0 :
        right -= 1

    elif liqSum < 0 :
        left += 1

    else : # liqSum == 0
        break

print(*ans)
