import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().rstrip())

cnt_0 = [-1 for _ in range(41)]
cnt_1 = [-1 for _ in range(41)]

def fib(n) :
    if n == 0 :
        cnt_0[0] = 1
        cnt_1[0] = 0
        return(cnt_0[0], cnt_1[0])
    elif n == 1 :
        cnt_0[1] = 0
        cnt_1[1] = 1
        return (cnt_0[1], cnt_1[1])
    else :
        if cnt_0[n] == -1 and cnt_1[n] == -1 :
            cnt_0[n] = fib(n - 1)[0] + fib(n - 2)[0]
            cnt_1[n] = fib(n - 1)[1] + fib(n - 2)[1]
        return(cnt_0[n], cnt_1[n])


for _ in range(n) :
    print(*fib(int(sys.stdin.readline().rstrip())))
