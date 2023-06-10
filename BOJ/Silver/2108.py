import sys, math
input = sys.stdin.readline

N = int(input().rstrip()) # 수의 개수 N
nums = [0] * N # 입력되는 수의 개수
nsum = 0
for i in range(N) :
    nums[i] = int(input().rstrip())
    nsum += nums[i]

nums.sort()
dict = {}
max_cnt = 0
for n in nums :
    if dict.get(str(n)) == None : dict[str(n)] = 1
    else : dict[str(n)] += 1

    if dict[str(n)] > max_cnt :
        max_cnt = dict[str(n)]

# 최빈값 찾기
modes = []
mode = 0
for key, value in dict.items() :
    if value == max_cnt :
        modes.append(int(key))

if len(modes) == 1 : mode = modes[0]
else : mode = modes[1]

# 정답 출력
print(round(nsum / N)) # 산술평균
print(nums[(N - 1) // 2]) # 중앙값
print(mode)
print(nums[-1] - nums[0]) # 범위
