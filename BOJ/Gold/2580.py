import sys
input = sys.stdin.readline

# 가로, 세로, 정사각형 이용해서 후보 구하고
# 넣고 아니면 백트레킹

sdk = [list(map(int, input().rstrip().split())) for _ in range(9)]

zeros = [] # 채워야하는 칸들
cnt = 0 # 몇칸 채워야 하는지
for r in range(9) :
    for c in range(9) :
        if sdk[r][c] == 0 :
            cnt += 1
            zeros.append((r, c))

def check(now, r, c) :
    result = [] # 후보가 될 수 있는 숫자들

    used = [0] * 10
    for i in range(9) : used[now[i][c]] += 1
    for i in range(9) : used[now[r][i]] += 1
    for i in range(r - r % 3, r - r % 3 + 3) :
        for j in range(c - c % 3, c - c % 3 + 3) :
            used[now[i][j]] += 1

    for i in range(1, 10) :
        if used[i] == 0 : result.append(i)

    return result

def backtracking(res, depth) :

    if depth == cnt :
        for s in res: print(*s)
        sys.exit(0)

    cr, cc = zeros[depth]
    possible = check(res, cr, cc) # 후보키를 구함

    for p in possible :
        res[cr][cc] = p
        backtracking(res, depth + 1) # 다음 위치 구하러 ㄱㄱ
        res[cr][cc] = 0

backtracking(sdk, 0)
