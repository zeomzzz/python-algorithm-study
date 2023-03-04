bingo = []
for _ in range(5) :
    line = list(map(int, input().split()))
    bingo.append(line)

check = [0] * 16
# idx 5 :대각선(좌하향), 15:대각선(우하향), 0~4 : 세로, 10~14 : 가로

cnt = 0 # 사회자가 부른 수의 개수
isBingo = False

# 사회자가 부른 숫자
nums = []
for _ in range(5) :
    tmp = list(map(int, input().split()))
    for i in tmp : nums.append(i)

for n in nums :
    for r in range(5) :
        for c in range(5) :
            if bingo[r][c] == n :
                check[r] += 1
                check[10 + c] += 1
                if r == c : check[15] += 1
                if r + c == 4 : check[5] += 1
                cnt += 1

                # 빙고 확인
                bingoCnt = 0
                for i in check :
                    if i == 5 :
                        bingoCnt += 1
                        # 빙고 3개면 종료
                        # check를 모두 확인하면 bingoCnt가 3개 초과일 수 있으므로 if문 하위에서 확인
                        if bingoCnt == 3:
                            isBingo = True
                            break
                            
            if isBingo : break
        if isBingo : break
    if isBingo : break

print(cnt)
