import sys

n = int(sys.stdin.readline().rstrip())
size = []

for i in range(n) :
    x, y = map(int, sys.stdin.readline().rstrip().split())
    size.append([x, y])

for i in size :
    rank = 1
    for j in size :
        # j의 몸무게, 키 모두가 i보다 크면 i는 순위 밀림
        if i[0] < j[0] and i[1] < j[1] : rank += 1
    print(rank, end = " ")
