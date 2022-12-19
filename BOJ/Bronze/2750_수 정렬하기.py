# 풀이 1 : sort

n = int(input())
lst = []

for i in range(n) :
    lst.append(int(input()))

lst.sort()

for j in lst :
    print(j)

    
# 풀이 2 : 버블 정렬

n = int(input())
lst = []

for i in range(n) :
    lst.append(int(input()))

for j in range(len(lst)) :
    for k in range(j+1, len(lst)) :
        if lst[j] > lst[k] :
            lst[j], lst[k] = lst[k], lst[j]

for l in lst :
    print(l)
 

# 풀이 3 : 삽입 정렬

n = int(input())
lst = []

for i in range(n) :
    lst.append(int(input()))

for j in range(1, len(lst)) :
    while j > 0 and lst[j] < lst[j -1] :
        lst[j], lst[j-1] = lst[j-1], lst[j]

        j -= 1

for l in lst :
    print(l)
