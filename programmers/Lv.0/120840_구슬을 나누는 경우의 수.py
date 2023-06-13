def solution(balls, share):
    
    def fact(n) :
        n_fact = 1
        for i in range(1, n+1) :
            n_fact *= i
        
        return n_fact
    
    answer = fact(balls) / (fact(balls-share) * fact(share))
    
    return answer
