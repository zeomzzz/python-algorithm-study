x = int(input())

i = 0
a = x

while True :
    a = (a % 10) * 10 + (a // 10 + a % 10) % 10
    i += 1
    if a == x :
        break

print(i)
