from collections import deque
import sys

T = int(sys.stdin.readline().rstrip()) # tc

for _ in range(T) :
    p_lst = list(sys.stdin.readline().rstrip()) # 함수 p 리스트
    n = int(sys.stdin.readline().rstrip()) # 배열에 들어 있는 수의 개수
    arr = sys.stdin.readline().rstrip() # 정수 들어 있는 배열

    isError = False # 에러 발생 판단
    reverse = 1 # 최종적으로 1이면 뒤집지 않음, -1이면 되집음

    # 입력이 빈 배열인 경우에 대한 처리
    # 함수 하나라도 D이면 error
    # 함수 모두 R이면 빈 배열 반환
    if arr == "[]" :
        arr = []
        if "D" in p_lst :
            isError = True

    else :
        arr = arr.replace("[", "").replace("]", "").split(",")
        dqArr = deque(arr)

        for i in p_lst :
            # 함수 R : 배열 뒤집기
            if i == "R" :
                reverse *= (-1)
            # 함수 D : 맨 앞 정수 버림. 단, 배열 크기 0이면 오류
            else :
                if len(dqArr) > 0 :
                    if reverse == 1 :
                        dqArr.popleft()
                    else :
                        dqArr.pop()
                else :
                    isError = True
                    break

    # isError == True 이면 에러 출력, 아닌 경우 함수 수행한 배열 출력
    if isError :
        print("error")

    else:

        if arr == [] or list(dqArr) == [] :
            print("[]")
        else :
            arr = list(dqArr)
            if reverse == -1:
                arr = arr[::-1]

            # 출력 형식 예시와 동일하게
            ans = "["
            for i in arr:
                ans += i + ","
            ans = ans[:-1] + "]"

            print(ans)
