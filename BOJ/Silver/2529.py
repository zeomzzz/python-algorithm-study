import sys
input = sys.stdin.readline

k = int(input())  # k : 부등호 문자의 개수
signs = list(input().split())

minn = 10 ** 10
maxx = -1 * minn

def backtracking(prev, depth) :
    global minn, maxx

    # base
    if depth == k :
        tmp = ''
        for a in ans : tmp += str(a)
        tmp = int(tmp)

        minn = min(minn, tmp)
        maxx = max(maxx, tmp)
        return

    # recursive
    else :
        for i in range(10) :
            if i not in ans :
                if (signs[depth] == '>' and prev > i) or (signs[depth] == '<' and prev < i) :
                    ans.append(i)
                    backtracking(i, depth + 1)
                    ans.pop()


for i in range(10) :
    ans = [i]
    backtracking(i, 0)

l = len(str(maxx)) - len(str(minn))

print(maxx)
print('0' * l + str(minn))
