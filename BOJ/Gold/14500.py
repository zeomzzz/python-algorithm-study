import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # N : 세로, M : 가로
paper = [list(map(int, input().rstrip().split())) for _ in range(N)]
paper_spinned = [[0] * N for _ in range(M)]
for r in range(M) :
    for c in range(N) :
        paper_spinned[r][c] = paper[c][r]

max_sum = 0

# 테트로미노를 돌리기보다는
# 종이를 돌린다 (이게 더 쉬우니까)

# 1번은 회전만 확인(처음, 90도)
# 2, 3, 4, 5 : 2*3 영역에서 4개 선택 - 5개 경우. 90도 회전만 더 확인

def find1(square, r, c) :
    tmp_max = 0

    for i in range(r) :
        for j in range(c - 3) :
            tmp = square[i][j] + square[i][j+1] +  square[i][j+2] + square[i][j+3]
            tmp_max = max(tmp_max, tmp)

    return tmp_max

def find_rest(square, r, c) :
    tmp = []

    # 6개 sum을 구함
    tmp_sum = 0

    for i in range(r - 2) :
        for j in range(c - 1) :
            tmp_sum = square[i][j] + square[i+1][j] + square[i+2][j] + square[i][j+1] + square[i+1][j+1] + square[i+2][j+1]

            global tmp_lst, tmp_combi
            tmp_lst = []
            tmp_combi = []
            combi(i, j, 0, 0, 0, square)

            find2_lst = find2(i, j, square)

            for k in range(len(find2_lst)) :
                tmp_combi.remove(find2_lst[k])

            tmp_combi.sort()

            tmp.append(tmp_sum - tmp_combi[0])

    tmp.sort(reverse = True)

    return tmp[0]


tmp_lst = []
tmp_combi = []
def combi(r, c, depth, tmp_sum, idx, square) :

    if depth == 2 :
        tmp_combi.append(tmp_sum)
        return

    squares = [(r, c), (r+1, c), (r+2, c), (r, c+1), (r+1, c+1), (r+2, c+1)]

    for i in range(idx, 6) :
        cr, cc = squares[i]
        tmp_sum += square[cr][cc]

        combi(r, c, depth+1, tmp_sum, i + 1, square)

        tmp_sum -= square[cr][cc]

def find2(r, c, square) :
    tmp_lst = []

    tmp_lst.append(square[r+1][c] + square[r+1][c+1])
    tmp_lst.append(square[r][c] + square[r+1][c+1])
    tmp_lst.append(square[r][c+1] + square[r+1][c])
    tmp_lst.append(square[r+1][c] + square[r+2][c+1])
    tmp_lst.append(square[r+1][c+1] + square[r+2][c])

    return tmp_lst

print(max(max(find1(paper, N, M), find1(paper_spinned, M, N)), max(find_rest(paper, N, M), find_rest(paper_spinned, M, N))))
