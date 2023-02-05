# 연산의 우선순위 : 분배법칙 활용

import sys

lst = list(sys.stdin.readline().rstrip())
stack = []
result = 0

for i in range(len(lst)) :
    if lst[i] in ["(", "["] :
        stack.append(lst[i])

    else : # lst[i] in [")", "]"]

        if len(stack) == 0 :
            result = 0
            break

        else :

            if lst[i] == ")" :
                if stack[-1] == "(" :
                    stack.pop()

                    if lst[i-1] == "(" :
                        n = 2

                        for j in stack :
                            if j == "(" :
                                n *= 2
                            elif j == "[" :
                                n *= 3

                        result += n

                else : # stack[-1] == "["
                    result = 0
                    break

            else : # lst[i] == "]"
                if stack[-1] == "[" :
                    stack.pop()

                    if lst[i-1] == "[" :
                        n = 3

                        for j in stack :
                            if j == "(" :
                                n *= 2
                            elif j == "[" :
                                n *= 3

                        result += n

                else : # stack[-1] == "("
                    result = 0
                    break

if len(stack) != 0 :
    result = 0

print(result)
