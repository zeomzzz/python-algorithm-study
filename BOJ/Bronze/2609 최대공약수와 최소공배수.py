# 풀이 1

nums = list(map(int, input().split()))

a = min(nums)
b = max(nums)

for i in range(a) :
    if a % (a - i) == 0 and b % (a - i) == 0 :
        print(a - i)
        break

for j in range(1, a + 1) :
    if (b * j) % a == 0 :
        print(b * j)
        break

        
# 풀이 2 : math 모듈 이용

import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))


# 풀이 3 : 유클리드 호제법

nums = list(map(int, input().split()))

a, b = max(nums), min(nums)

def gcd(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))
