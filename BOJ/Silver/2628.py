c, r = map(int,input().split()) # c : 가로, r : 세로
n = int(input()) # 칼로 잘라야 하는 점선의 개수

# 0 ~ +1(양 끝) 만들고 끝은 잘림 표시
paper_c = [0] * (c + 1)
paper_c[0] = 1
paper_c[-1] = 1

paper_r = [0] * (r + 1)
paper_r[0] = 1
paper_r[-1] = 1

# 자른 곳 표시
for _ in range(n) :
    a, num = map(int, input().split())

    if a == 0 : # 0 : 가로로 자름 -> 세로에 잘림 표시(r)
        paper_r[num] = 1
    else : # a == 1
        paper_c[num] = 1

# 가로, 세로에서 가장 긴 길이 찾기
max_c = 0
max_r = 0
tmp = 1

# 가로로 잘림 : 세로에 잘림 표시
for i in paper_r :
    if i == 0 :
        tmp += 1
    else : # i == 1 (잘림 표시)
        if tmp > max_r :
            max_r = tmp
        tmp = 1 # 초기화

for i in paper_c :
    if i == 0 :
        tmp += 1
    else :
        if tmp > max_c :
            max_c = tmp
        tmp = 1

print(max_c * max_r)
