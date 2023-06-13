# 3x 마을의 1 ~ 100 리스트 만들고 인덱스 이용하여 answer 반환

# 리스트 만드는 방법 1 : 3의 배수 아님 & 10으로 나누어 나머지 3 아님 (각 자리수에 3이 없음)

def solution(n):
    town_num = []
    i = 1
    
    while len(town_num) < 101 :
        if i % 3 != 0 :
            if i % 10 != 3 :
                if (i // 10) % 10 != 3 :
                    town_num.append(i)
                    i += 1
                else :
                    i += 1
            else :
                i += 1
        else :
            i += 1
        
    answer = town_num[n - 1]
    
    return answer


# 리스트 만드는 방법 2 : 3의 배수 아님 & str로 바꾸었을 떄 3 없음

def solution(n):
    answer = 0
    town_num = []
    i = 1
    
    while len(town_num) < 101 :
        if i % 3 != 0 and '3' not in str(i) :
            town_num.append(i)
        i += 1
    
    answer = town_num[n - 1]
    
    return answer
