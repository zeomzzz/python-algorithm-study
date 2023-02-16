import sys

n = int(sys.stdin.readline().rstrip())
n_lst = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_lst = list(map(int, sys.stdin.readline().rstrip().split()))

dic = {}
ans = []

for key in n_lst :
    if key in dic :
        dic[key] += 1
    else :
        dic[key] = 1

for target in m_lst :
    cnt = dic.get(target)

    if cnt == None:
        ans.append(0)
    else :
        ans.append(cnt)

print(*ans)
