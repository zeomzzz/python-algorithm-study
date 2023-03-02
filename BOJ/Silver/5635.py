import sys

n = int(sys.stdin.readline().rstrip()) # 학생 수
lst = [[0, 0, 0, 0] for _ in range(n)]
days_lst = []
for i in range(n) :
    name, d, m, y = sys.stdin.readline().rstrip().split()
    lst[i][0] = name
    lst[i][1] = int(d)
    lst[i][2] = int(m)
    lst[i][3] = int(y) - 1990
    days = lst[i][3] * 365 + (lst[i][2] - 1) * 31 + lst[i][1]
    days_lst.append(days)

min_idx = 0
max_idx = 0

for i in range(1, n) :
    if days_lst[i] < days_lst[min_idx] :
        min_idx = i
    if days_lst[max_idx] < days_lst[i] :
        max_idx = i

# 1990년을 기준으로 며칠 째에 태어났는지 -> days가 클 수록 어림
print(lst[max_idx][0])
print(lst[min_idx][0])
