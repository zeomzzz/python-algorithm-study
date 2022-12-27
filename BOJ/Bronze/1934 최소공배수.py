T = int(input())

for i in range(T) :
    nums = list(map(int, input().split()))
    A, B = max(nums), min(nums)

    def gcd(A, B) :
        while B > 0 :
            A, B = B, A % B
        return A
    
    print(int(A * B / gcd(A, B)))
