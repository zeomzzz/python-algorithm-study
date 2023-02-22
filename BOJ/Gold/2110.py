n, c = map(int, input().split())  # n : 집의 개수, c : 공유기의 개수

pos = []  # pos에 주어진 공유기의 위치를 오름차순으로 저장
for _ in range(n):
    p = int(input())
    pos.append(p)
pos.sort()

# 이분 탐색을 이용하여 두 공유기 사이의 거리를 구함

start = 1  # 공유기 사이의 최소 거리
end = pos[-1] - pos[0]  # 공유기 사이의 최대 거리

while end >= start:
    mid = (start + end) // 2  # 첫 최소 거리가 mid라고 가정하고

    # x에 공유기 위치
    x = pos[0]  # 첫번째 공유기 위치
    cnt = 1  # 공유기 개수 cnt

    for i in range(1, n):
        if x + mid <= pos[i]:  # 다음 공유기까지의 거리가 mid 이상
            x = pos[i]
            cnt += 1

    if cnt < c:  # 지금 거리로 설치한 공유기 수가 설치하려는 공유기 수보다 적으면
        end = mid - 1  # 거리를 더 가깝게 조정해봄
    else:  # c 이상 설치했으면
        ans = mid  # 정답이라고 가정하고
        start = mid + 1  # 거리가 더 멀어질 수도 있는지 확인

print(ans)
