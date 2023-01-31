N = int(input())

for t in range(N):
    s = input()
    ans = "YES"

    if s.count("(") != s.count(")"):
        ans = "NO"
    else:
        for i in range(1, len(s)):
            s1 = s[:i]
            if s1.count("(") < s1.count(")"):
                ans = "NO"
                break
                
    print(ans)
