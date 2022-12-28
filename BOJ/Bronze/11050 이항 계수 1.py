N, k = map(int, input().split())

def factorial(n) :
    result = 1
    if n == 0 :
        result = 1
    else :
        result = factorial(n-1) * n
    return result

answer = int(factorial(N) / (factorial(k) * factorial(N-k)))

print(answer)
