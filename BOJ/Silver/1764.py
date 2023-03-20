import sys
input = sys.stdin.readline

n, m = map(int, input().split())
unheard = set()
unseen = set()

for _ in range(n) :
    unheard.add(input().rstrip())

for _ in range(m) :
    unseen.add(input().rstrip())

lst = list(unheard.intersection(unseen))
lst.sort()

print(len(lst))
for i in lst :
    print(i)
