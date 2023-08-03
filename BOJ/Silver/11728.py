import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ans = list(map(int, input().rstrip().split())) + list(map(int, input().rstrip().split()))
ans.sort()

print(' '.join(map(str, ans)))
