import sys
input = sys.stdin.readline

word = input().rstrip()

# 사전순으로 가장 앞서는 == AAAA로 채울 수 있으면 이거로 채워야

word = word.replace("XXXX", "AAAA")
word = word.replace("XX", "BB")

if 'X' in word :
    print(-1)
else :
    print(word)
