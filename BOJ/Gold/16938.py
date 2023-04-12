import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
# N : 문제 개수, L : 난이도의 합 하한선(이상), R : 상한선(이하), X : 차이 하한선(이상)
lvs = list(map(int, input().split())) # 문제 난이도
cnt = 0

for i in range(1, 1 << N) :
    flag = True
    summ = 0
    minn = 1e9
    maxx = 0

    for j in range(N) :
        if i & (1 << j) :
            minn = min(minn, lvs[j])
            maxx = max(maxx, lvs[j])
            summ += lvs[j]
            if summ > R :
                flag = False
                break

    if not flag or minn == maxx or summ < L or maxx - minn < X :
        continue

    cnt += 1

print(cnt)
