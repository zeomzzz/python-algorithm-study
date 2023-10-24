def solution(people, limit):
    answer = 0
    # 몸무게 오름차순 정렬
    people.sort()
    
    # 투포인터로 담기
    start = 0
    end = len(people) - 1
    
    while start <= end :
        if start == end :
            answer += 1
            break
        elif people[start] + people[end] <= limit : # 둘 다 탑승
            answer += 1
            start += 1
            end -= 1
        else : # 무거운 사람만 탑승
            answer += 1
            end -= 1
    
    return answer
