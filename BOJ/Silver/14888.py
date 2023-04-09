import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) # 연산자 개수 : +, -, *, /
chosen = [0, 0, 0, 0] # 고른 연산자 개수 저장

ans_min = 1e9
ans_max = -1e9

def cal(a, op, b) :
    match op :
        case 0 : return a + b
        case 1 : return a - b
        case 2 : return a * b
        case 3 :
            if a < 0 and b > 0 : # 음수//양수 : 문제 설명
                return (a * (-1) // b) * (-1)
            else :
                return a // b


def backtracking(res, depth) :
    global ans_max, ans_min

    # base
    if depth == n - 1 :
        ans_max = max(ans_max, res)
        ans_min = min(ans_min, res)

    # recursive
    else :
        for i in range(4) : # 연산자 고르기(+, -, *, //)
            if chosen[i] + 1 > ops[i] : # 연산자 골랐을 때 개수 제한 넘어가면 컨티뉴
                continue
            else : # 고를 수 있는 경우
                chosen[i] += 1 # 골랐다 체크
                backtracking(cal(res, i, nums[depth + 1]), depth + 1)

                chosen[i] -= 1 # 복구

backtracking(nums[0], 0)

print(ans_max)
print(ans_min)
