n = int(input())

for i in range(n) :
    x = input()
    cnt = 0

    def recursion(x, l, r) :
        global cnt
        cnt += 1
        if l >= r : return 1
        elif x[l] != x[r] : return 0
        else : return recursion(x, l+1, r-1)
    
    def isPalindrome(x) :
        return recursion(x, 0, len(x)-1)
    
    print(isPalindrome(x), cnt)
