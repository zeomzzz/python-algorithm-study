# 풀이 1

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


# 풀이 2 : 스택 이용

T = int(input())

for _ in range(T) :
    lst = list(input())
    stack = []
    isVPS = True

    for i in range(len(lst)) :
        if lst.pop() == ")" :
            stack.append(")") # lst 맨 끝이 ) 인 경우 stack에 추가
        else :
            if len(stack) > 0 : # stack에 pop할 ) 있음
               stack.pop() # lst 맨 끝이 ( 인 경우 stack의 ) 제거 (쌍 맞춤)
            else :
                isVPS = False
                break # 맨 끝이 (이었는데 pop 할 ) 없으면 VPS 아님 & 반복문 종료

    if len(stack) == 0 and isVPS : # VPS이려면 위 반복문 중간에 break되지 않고 stack 모두 비워야 함 (쌍이 모두 맞음)
        print("YES")
    else :
        print("NO")
        
        
# 풀이 3 : 스택 + readline

import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    lst = list(sys.stdin.readline().rstrip())
    stack = []
    isVPS = True

    for i in range(len(lst)) :
        if lst.pop() == ")" :
            stack.append(")") # lst 맨 끝이 ) 인 경우 stack에 추가
        else :
            if len(stack) > 0 : # stack에 pop할 ) 있음
               stack.pop() # lst 맨 끝이 ( 인 경우 stack의 ) 제거 (쌍 맞춤)
            else :
                isVPS = False
                break # 맨 끝이 (이었는데 pop 할 ) 없으면 VPS 아님 & 반복문 종료

    if len(stack) == 0 and isVPS : # VPS이려면 위 반복문 중간에 break되지 않고 stack 모두 비워야 함 (쌍이 모두 맞음)
        print("YES")
    else :
        print("NO")
