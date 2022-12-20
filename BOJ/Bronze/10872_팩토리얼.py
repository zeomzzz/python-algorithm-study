# 풀이 1 : for 문

n = int(input())
x = 1

for i in range(n) :
    x *= n - i

print(x)


# 풀이 2 : 재귀함수

def factorial(n) :
    result = 1

    if n > 0 :
        result = n * factorial(n-1)
    
    return result

n = int(input())
print(factorial(n))
