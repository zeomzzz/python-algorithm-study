def solution(n, m):
    
    # 최대공약수 (gcd)
    min_num = min(n, m)
    
    while True :
        if n % min_num == 0 and m % min_num == 0 :
            gcd = min_num
            break
        else :
            min_num -= 1
    
    # 최소공배수 (lcm) : 최대공약수-최소공배수의 관계 이용
    lcm = n * m / gcd
    
    return [gcd, lcm]
