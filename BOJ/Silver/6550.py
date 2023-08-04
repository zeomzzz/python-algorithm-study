import sys
input = sys.stdin.readline

while True :
    st = input().rstrip()

    if len(st) == 0 : break

    s, t = st.split()
    # t에서 문자 몇 개가 빠지는 건 괜찮지만,
    # 순서는 맞아야 한다

    idx_s, idx_t = 0, 0
    ans = "Yes"

    if len(s) > len(t) : ans = "No"

    else :
        while True :
            if s[idx_s] == t[idx_t] :
                idx_s += 1
                idx_t += 1
            else :
                idx_t += 1

            if idx_s == len(s) or idx_t == len(t) : break

        if idx_s != len(s) : ans = "No"

    print(ans)
