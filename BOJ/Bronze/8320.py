import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 조정

def square(n) : # n개를 모두 사용하는 경우의 수를 cnt 하는 함수
    cnt = 0

    for i in range(1, int(n ** (1/2)) + 1) : # 중복을 만들지 않는 직사각형의 한 변의 길이의 범위
        if n % i == 0 : # 나누어 떨어져야 가능한 경우임
            cnt += 1

    return cnt


def sum_square(n) :

    if n == 1 :
        return 1
    else : # 이 전까지의 경우 + n개 모두 사용했을 때의 경우
        return sum_square(n-1) + square(n)

n = int(sys.stdin.readline().rstrip())

print(sum_square(n))
