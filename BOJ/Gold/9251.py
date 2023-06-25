import sys
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

A.insert(0, 0)
B.insert(0, 0)

l1 = len(A)
l2 = len(B)

lcs = [[0] * l1 for _ in range(l2)]
l = 0
cr, cc = 0, 0

for r in range(1, l2) :
    for c in range(1, l1) :

        if B[r] == A[c] :
            lcs[r][c] = lcs[r-1][c-1] + 1

            if lcs[r][c] > l : # lcs 길어지면 갱신
                l += 1
                cr, cc = r, c

        else :
            lcs[r][c] = max(lcs[r-1][c], lcs[r][c-1])

print(l)
