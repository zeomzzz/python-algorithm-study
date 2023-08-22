import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
sets = list(map(int, input().rstrip().split()))
tmp = list(map(int, input().rstrip().split()))
sets += tmp
sets = list(set(sets))

ans = A + B - 2 * (A + B - len(sets))

print(ans)
