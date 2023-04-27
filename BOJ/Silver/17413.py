from collections import deque
import sys
input = sys.stdin.readline

S = list(input().rstrip())
word = []
tag = deque()
ans = ''

for s in S :
    if s == '<' :
        if word :
            while word :
                ans += word.pop()

        tag.append(s)
    elif s != '>' and tag :
        tag.append(s)
    elif s == '>' :
        tag.append(s)

        while tag :
            ans += tag.popleft()

    else :
        if s == ' ' :
            while word :
                ans += word.pop()
            ans += s
        else : word.append(s)

if word :
    while word :
        ans += word.pop()

print(ans)
