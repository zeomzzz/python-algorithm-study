import sys
input = sys.stdin.readline

T = int(input().rstrip())
n = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
B = list(map(int, input().rstrip().split()))

# A의 부 배열 합 구하고 + dict에 개수 저장
# B의 부 배열 구하면서 A의 부배열과 합해서 T가 되는지 확인

Asums = {}
Bsums = {}

ans = 0

# A부터 부 배열의 합 구하기
for i in range(n) :
    s = A[i]

    if str(s) in Asums : Asums[str(s)] += 1
    else : Asums[str(s)] = 1

    for j in range(i + 1, n) :
        s += A[j]

        if str(s) in Asums: Asums[str(s)] += 1
        else: Asums[str(s)] = 1

# B부터 부 배열의 합 구하기
for i in range(m):
    s = B[i]
    if str(T - s) in Asums : ans += Asums[str(T - s)]

    for j in range(i + 1, m):
        s += B[j]
        if str(T - s) in Asums : ans += Asums[str(T - s)]

print(ans)
