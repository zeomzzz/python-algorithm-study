n = int(input())

def ball_game(trial, strike, ball) :
    global num_lst
    score = strike * 10 + ball
    a = trial // 100  # 100의 자리
    b = trial // 10 % 10  # 10의 자리
    c = trial % 10  # 1의 자리
    tmp_lst = []
    tmp_score = 0

    # num_lst의 숫자와 trial 비교해서 strike, ball 일치하는 경우만 num_lst에 남김
    for i in num_lst :
        na  = i // 100  # 100
        nb = i // 10 % 10  # 10
        nc = i % 10  # 1
        n_lst = [na, nb, nc]

        # 3 strike
        if na == a and nb == b and nc == c :
            tmp_score = 30
        # 2 strike 0 ball (2 strike 1 ball 은 불가능)
        elif (na == a and nb == b and nc != c) or (na == a and nb != b and nc == c) \
                or (na != a and nb == b and nc == c) :
            tmp_score = 20
        # 1 strike 2 ball
        elif (na == a and nb == c and nc == b) or (nb == b and na == c and nc == a) \
                or (nc == c and na == b and nb == a) :
            tmp_score = 12
        # 1 strike 1 ball
        elif ((na == a and ((nb == c and nc != b) or (nc == b and nb != c)))
        or (nb == b and ((na == c and nc != a) or (nc == a and na != c)))
        or (nc == c and ((na == b and nb != a) or (nb == a and na != b)))) :
            tmp_score = 11
        # 1 strike 0 ball
        elif ((na == a and nb != b and nb != c and nc != b and nc != c)
        or (nb == b and na != a and na != c and nc != a and nc != c)
        or (nc == c and na != a and na != b and nb != a and nb != b)) :
            tmp_score = 10
        # 0 strike 3 ball
        elif trial in [100 * nb + 10 * nc + na, 100 * nc + 10 * na + nb] :
            tmp_score = 3
        # 0 strike 2 ball
        elif (a in n_lst and b in n_lst and c not in n_lst) or (b in n_lst and c in n_lst and a not in n_lst) or (a in n_lst and c in n_lst and b not in n_lst) :
            tmp_score = 2
        # 0 strike 0 ball
        elif a not in n_lst and b not in n_lst and c not in n_lst :
            tmp_score = 0
        # 0 strike 1 ball
        else :
            tmp_score = 1

        if tmp_score == score :
            tmp_lst.append(i)

    num_lst = tmp_lst[:]


num_lst = [] # 가능한 모든 숫자의 경우의 수
for i in range(1, 10):
    for j in range(1, 10) :
        for k in range(1, 10) :
            if i != j and j !=k and i != k :
                num = 100 * i + 10 * j + k
                num_lst.append(num)

for _ in range(n) :
    trial, strike, ball = map(int, input().split())
    ball_game(trial, strike, ball)

ans = len(num_lst)

print(ans)
# print(num_lst)
