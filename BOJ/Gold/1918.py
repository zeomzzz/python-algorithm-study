import sys

# 중위 표기식을 토큰 단위로 쪼개서 리스트에 넣음
exp_lst = list(sys.stdin.readline().rstrip()[:])
ans = ""
pri_dict = {'*' : 2, "/" : 2, "+" : 1, "-" : 1}
stack = []

for i in exp_lst :

    if ord("Z") >= ord(i) >= ord("A") : # 피연산자이면 출력
        ans += i
    else :
        if i == "(" : # 여는 괄호는 stack에 추가
            stack.append(i)
        elif i == ")" : # stack의 여는 괄호 만날때까지 pop
            while stack[-1] != "(" :
                ans += stack.pop()
            stack.pop()
        else :
            while len(stack) > 0 and stack[-1] != "(" and pri_dict[i] <= pri_dict[stack[-1]] :
                ans += stack.pop()
            stack.append(i)

while len(stack) > 0 :
    ans += stack.pop()

print(ans)
