import sys
input = sys.stdin.readline

n = int(input().rstrip())
stack = []
num_lst = [i for i in range(n, 0, -1)]
ans = []
flag = True

for _ in range(n) :

    if not flag :
        ans = ["NO"]
        break

    a = int(input().rstrip())

    while True :

        if not len(stack) :
            if len(num_lst) :
                stack.append(num_lst.pop())
                ans.append("+")
            else :
                flag = False
                break
        else :
            tmp = stack[-1]

            if tmp < a :
                if len(num_lst):
                    stack.append(num_lst.pop())
                    ans.append("+")
                else:
                    flag = False
                    break
            elif tmp == a :
                stack.pop()
                ans.append("-")
                break
            else :
                flag = False
                break

for a in ans : print(a)
