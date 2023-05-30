import sys
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())

lst = [list(map(int, input().rstrip().split())) for _ in range(N)]

def func1() :
    global lst

    m = len(lst[0])
    if m == N: n = M
    else: n = N

    nlst = lst[:]
    lst = [[0 for _ in range(m)] for _ in range(n)]

    for r in range(n) :
        for c in range(m) :
            lst[r][c] = nlst[n-r-1][c]

def func2() :
    global lst

    m = len(lst[0])
    if m == N: n = M
    else: n = N

    nlst = lst[:]
    lst = [[0 for _ in range(m)] for _ in range(n)]

    for r in range(n) :
        for c in range(m) :
            lst[r][c] = nlst[r][m-c-1]

def func3() :
    global lst

    m = len(lst[0])
    if m == N: n = M
    else: n = N

    nlst = lst[:]
    lst = [[0 for _ in range(n)] for _ in range(m)]

    for r in range(m) :
        for c in range(n) :
            lst[r][c] = nlst[n-c-1][r]

def func4() :
    global lst

    m = len(lst[0])
    if m == N: n = M
    else: n = N

    nlst = lst[:]
    lst = [[0 for _ in range(n)] for _ in range(m)]

    for r in range(m) :
        for c in range(n) :
            lst[r][c] = nlst[c][m-r-1]

def func5() :
    global lst

    m = len(lst[0])
    if m == N: n = M
    else: n = N

    nlst = lst[:]
    lst = [[0 for _ in range(m)] for _ in range(n)]

    # 1번 구역
    for r in range(n//2) :
        for c in range(m//2) :
            lst[r][c] = nlst[r+n//2][c]

    # 2번 구역
    for r in range(n//2) :
        for c in range(m//2, m) :
            lst[r][c] = nlst[r][c-m//2]

    # 3번 구역
    for r in range(n//2, n) :
        for c in range(m//2, m) :
            lst[r][c] = nlst[r-n//2][c]

    # 4번 구역
    for r in range(n//2, n) :
        for c in range(m//2) :
            lst[r][c] = nlst[r][c+m//2]


def func6() :
    global lst

    m = len(lst[0])
    if m == N: n = M
    else: n = N

    nlst = lst[:]
    lst = [[0 for _ in range(m)] for _ in range(n)]

    # 1번 구역
    for r in range(n//2) :
        for c in range(m//2) :
            lst[r][c] = nlst[r][c+m//2]

    # 2번 구역
    for r in range(n // 2):
        for c in range(m // 2, m):
            lst[r][c] = nlst[r+n//2][c]

    # 3번 구역
    for r in range(n//2, n) :
        for c in range(m//2, m) :
            lst[r][c] = nlst[r][c-m//2]

    # 4번 구역
    for r in range(n // 2, n):
        for c in range(m // 2):
            lst[r][c] = nlst[r-n//2][c]

cals = list(map(int, input().rstrip().split()))

for cal in cals :

    if cal == 1 : func1()
    elif cal == 2 : func2()
    elif cal == 3 : func3()
    elif cal == 4 : func4()
    elif cal == 5 : func5()
    elif cal == 6 : func6()

for l in lst :
    print(*l)
