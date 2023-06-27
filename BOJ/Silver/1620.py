import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

pmon = {}
for i in range(N) : # 딕셔너리에 저장
    name = input().rstrip()
    pmon[i + 1] = name
    pmon[name] = i + 1

for _ in range(M) :
    q = input().rstrip()

    if q.isalpha() : # 알파벳
        print(pmon[q])
    else :
        print(pmon[int(q)])
