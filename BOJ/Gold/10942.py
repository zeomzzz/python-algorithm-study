import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 수열의 크기 N
nums = list(input().rstrip().split()) # N개의 수
palin = [[0] * N for _ in range(N)]

# 펠린드롬 체크
# 1. 길이 홀수인 경우
for i in range(N) :
    palin[i][i] = 1
    start = i - 1
    end = i + 1

    while start >= 0 and end < N :
        if palin[start + 1][end - 1] == 1 and nums[start] == nums[end]:
            palin[start][end] = 1
            start -= 1
            end += 1

        else : break

# 2. 길이 짝수인 경우
for i in range(N - 1) :
    start = i
    end = i + 1

    if nums[start] == nums[end] :
        palin[start][end] = 1

    start -= 1
    end += 1

    while start >= 0 and end < N:
        if palin[start + 1][end - 1] == 1 and nums[start] == nums[end] :
            palin[start][end] = 1
            start -= 1
            end += 1
        else : break

M = int(input().rstrip()) # 질문의 갯수

for i in range(M) :
    S, E = map(int, input().rstrip().split()) # 질문 S, E
    print(palin[S - 1][E - 1])
