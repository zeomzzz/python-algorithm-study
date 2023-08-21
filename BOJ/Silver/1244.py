import sys
input = sys.stdin.readline

switch_num = int(input().rstrip()) # 스위치 개수
switches = list(map(int, input().rstrip().split())) # 스위치들의 상태
switches.insert(0, 0)
N = int(input().rstrip()) # 학생수

for _ in range(N) :
    gender, num = map(int, input().rstrip().split())

    match gender :
        case 1 :
            for idx in range(num, switch_num + 1, num) :
                if switches[idx] == 0 : switches[idx] = 1
                else : switches[idx] = 0
        case 2 :
            if switches[num] == 0: switches[num] = 1
            else: switches[num] = 0

            tmp = 1
            while True :
                if num - tmp > 0 and num + tmp < switch_num + 1 and switches[num - tmp] == switches[num + tmp] :
                    if switches[num - tmp] == 1 : switches[num - tmp] = 0
                    else : switches[num - tmp] = 1

                    if switches[num + tmp] == 1 : switches[num + tmp] = 0
                    else : switches[num + tmp] = 1

                    tmp += 1

                else : break

ans = switches[1:]

cnt = 0
for a in ans :
    print(a, end = ' ')
    cnt += 1

    if cnt == 20 :
        print()
        cnt = 0
