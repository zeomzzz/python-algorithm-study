# 풀이 1 : 재귀함수

def f(n) :
    if n <= 1 :
        result = n
    elif n > 0 :
        result = f(n-1) + f(n-2)
    return result


x = int(input())
print(f(x))


# 풀이 2 : for 문 01

n = int(input())

f = [0, 1]

for i in range(2, n+1) :
    f.append(f[i-1] + f[i-2])

print(f[n])


# 풀이 3 : for 문 02

a, b = 0, 1

for i in range(int(input())) :
    a, b = b, a+b

print(a)
