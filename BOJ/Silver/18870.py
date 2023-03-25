import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
dict = {}

lst_sorted = sorted(list(set(lst)))
for i in range(len(lst_sorted)) :
    dict[lst_sorted[i]] = i

for l in lst :
    print(dict.get(l), end = " ")
