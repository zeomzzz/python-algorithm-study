n, m = map(int, input().split()) # 세로 n, 가로 m

floor = []
board = []

for i in range(n) :
    line = input()
    floor.append(line)

# 행 별로 판자 찾기
# "-" 담고 연달아 나오는건 안담음
# "|"는 다 담음(연달아 나오는 것 구분 위하여)
# "-"가 행 별로 몇 개인지 count 해서 리스트에 넣기
for r in range(n) :
    row_lst = []
    for c in range(m) :
        if len(row_lst) == 0 :
            row_lst.append(floor[r][c])
        else :
            if floor[r][c] == "|" :
                row_lst.append("|")
            else :
                if row_lst[-1] != "-" : row_lst.append("-")
    board.append(row_lst.count("-"))

# 열 별로 판자 찾기 (행 별로 한 방법과 같은 방법)
for c in range(m) :
    col_lst = []
    for r in range(n) :
        if len(col_lst) == 0 :
            col_lst.append(floor[r][c])
        else :
            if floor[r][c] == "-" :
                col_lst.append("-")
            else :
                if col_lst[-1] != "|" : col_lst.append("|")
    board.append(col_lst.count("|"))

sum = 0
for i in board :
    sum += i

print(sum)
