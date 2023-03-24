import sys
input = sys.stdin.readline

n = int(input())
syns = [list(map(int, input().split())) for _ in range(n)]
min_gap = 100 * 20 * 20

for i in range(1, 1 << (n - 1)) : # 부분집합 2^(n-1) - 1 개 확인
    team_s = []
    team_l = []
    sum_s = 0 # 스타트 팀의 합
    sum_l = 0 # 링크 팀의 합

    for j in range(n) : # n명에 대해서 확인
        if (i & (1 << j)) > 0 :
            for s in team_s :
                sum_s += syns[s][j]
                sum_s += syns[j][s]

            team_s.append(j)
        else :
            for l in team_l :
                sum_l += syns[l][j]
                sum_l += syns[j][l]

            team_l.append(j)
    
    min_gap = min(min_gap, abs(sum_s - sum_l))

print(min_gap)
