def solution(dots):
    answer = 0
    
    for i in range(0, 3) :
        
        # 1) dots의 원소 두 묶음으로 나눔
        dots_set1 = dots[0:3]
        dots_set2 = [dots[3]]
        
        dots_set2.append(dots_set1[i])
        del dots_set1[i]
        
        # 2) 각 묶음의 기울기 구해서 비교
        slope1 = (dots_set1[1][1] - dots_set1[0][1]) / (dots_set1[1][0] - dots_set1[0][0])
        slope2 = (dots_set2[1][1] - dots_set2[0][1]) / (dots_set2[1][0] - dots_set2[0][0])
        
        if slope1 == slope2 :
            answer = 1
            break
    
    return answer
