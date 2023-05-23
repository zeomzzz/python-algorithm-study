import sys
input = sys.stdin.readline

tc = int(input().rstrip())

for _ in range(tc) :
    letter = input().rstrip()
    l = len(letter)
    d = int(l ** (1/2))

    letter_lst = []
    i = 0

    for j in range(d) :
        tmp = []
        for k in range(d) :
            tmp.append(letter[i])
            i += 1
        letter_lst.append(tmp)

    lst = []
    for c in range(d) :
        for r in range(d - 1, -1, -1) :
            lst.append(letter_lst[r][c])

    ans = ''
    for i in range(len(lst) - 1, -1, -1) :
        ans += lst[i]

    print(ans)
