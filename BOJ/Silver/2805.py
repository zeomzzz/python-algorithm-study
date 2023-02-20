import sys

n, m = map(int, sys.stdin.readline().rstrip().split()) # 나무의 수 n, 나무의 길이 m

trees = list(map(int, sys.stdin.readline().rstrip().split())) # 나무 높이

end = max(trees)
start = end - m
ans = 0

while start <= end :
    mid = (end + start) // 2
    sum = 0

    for tree in trees :
        if tree - mid > 0 : # mid보다 나무가 낮으면 잘린 부분이 없으므로 음수 나올 수 없음
            sum += (tree - mid)

    if sum < m :
        end = mid - 1
    else :
        ans = mid
        start = mid + 1 # 더 높여도 되는지 확인

print(ans)
