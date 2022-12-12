total, n = int(input()), int(input())

i = 0
sum = 0

while i < n :
    price, num = map(int, input().split())
    sum += price * num
    i += 1

if total - sum : print("No")
else : print("Yes")
