import sys
input = sys.stdin.readline

# 1. 괄호 짝짓기
lst = list(input().rstrip())
l = len(lst)
stack = []
idxStack = []

open = []
close = []

for i in range(l - 1, -1, -1) :
    if lst[i] == ')' :
        stack.append(lst[i])
        idxStack.append(i)
    elif lst[i] == '(' :
        stack.pop()
        close.append(idxStack.pop())
        open.append(i)

# 2. 조합 선택
pairCnt = len(open)
ans = []

for i in range(1, 1 << pairCnt) :
    idxRemove = []

    for j in range(pairCnt) :
        if (i & (1 << j)) != 0 :
            idxRemove.append(open[j])
            idxRemove.append(close[j])

    idxRemove.sort()

    tmp = ''
    idx = 0
    for j in range(l) :
        if idx < len(idxRemove) and j == idxRemove[idx] : idx += 1
        else : tmp += lst[j]

    ans.append(tmp)

    ans = list(set(ans))
    ans.sort()

for a in ans : print(a)
