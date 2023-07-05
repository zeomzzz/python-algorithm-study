import math
import sys
input = sys.stdin.readline

N, Hatk = map(int, input().rstrip().split()) # 방의 개수 N, 초기 공격력 Hatk

Hcur = 0
Hmin = 0

# Hmin이 1 되는 지점이 최소 체력,,

for i in range(N) :
    t, a, h = map(int, input().rstrip().split())

    match t :
        case 1 :
            Matk = a # 몬스터의 공격력
            Mhp = h # 몬스터의 생명력

            # 몬스터를 몇 번 공격해야하는지 구하기
            atkCnt = math.ceil(Mhp / Hatk)

            # 몬스터를 공격 -1 만큼 몬스터가 공격
            Hcur -= (atkCnt - 1) * Matk

        case 2 :
            Hatk += a # 용사의 공격력 증가
            Hcur += h # 체력 회복

            if Hcur > 0 : Hcur = 0 # 체력 max 이상으로는 회복 못함

    Hmin = min(Hmin, Hcur)  # min 갱신

if Hmin <= 0 : print(abs(Hmin) + 1)
else : print(Hmin)
