import sys
input = sys.stdin.readline

N, L = map(int, input().rstrip().split()) # 과일의 개수 N, 초기 길이 L
heights = list(map(int, input().rstrip().split()))
heights.sort()

idx = 0
while True :
    if heights[idx] <= L :
        L += 1
        idx += 1

        if idx == N : break

    else : break

print(L)
