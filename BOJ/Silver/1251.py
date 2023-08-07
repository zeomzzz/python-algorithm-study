import sys
input = sys.stdin.readline

word = list(input().rstrip())
length = len(word)

ans = []
for i in range(1, length - 1) :
    for j in range(i + 1, length) :
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        ans.append("".join(first + second + third))

print(min(ans))
