import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

A.sort()

start = 0
end = N - 1
absB = abs(A[start] + A[end])
B = A[start] + A[end]

while start < end :

    tmpB = A[start] + A[end]

    if absB > abs(tmpB) :
        B = tmpB
        absB = abs(tmpB)

    if tmpB > 0 : end -= 1
    elif tmpB < 0 : start += 1
    else : break

print(B)
