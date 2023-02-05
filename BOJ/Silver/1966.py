import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    # N : 문서의 개수, M : 찾는 문서 초기 인덱스
    N, M = map(int, sys.stdin.readline().rstrip().split())
    # queue : 우선순위를 담음
    queue = list(map(int, sys.stdin.readline().rstrip().split()))
    # idx : 찾는 문서의 인덱스
    idx = M
    # cnt : 몇 번째로 출력되는지 확인
    cnt = 0

    while True :
        # 1) 찾는 문서가 맨 앞일 때
        if idx == 0 :
            # 1-1) 이 문서의 중요도가 가장 높으면 pop & 종료 & 출력 횟수 count
            if max(queue) == queue[idx] :
                queue.pop(0)
                cnt += 1
                break
            # 1-2) 중요도 가장 높지 않으면 맨 뒤로 보냄 & 해당 문서의 인덱스 변수 조정
            else :
                queue.append(queue.pop(0))
                idx = len(queue) - 1
        # 2) 다른 문서가 맨 앞일 때
        else :
            # 2-1) 이 문서의 중요도가 가장 높으면 pop & 출력 횟수 count & 찾는 문서 인덱스 변수 조정
            if max(queue) == queue[0] :
                queue.pop(0)
                cnt += 1
                idx -= 1
            # 2-2 ) 중요도 가장 높지 않으면 이 문서 맨 뒤로 보냄 & 찾는 문서 인덱스 변수 조정
            else :
                queue.append(queue.pop(0))
                idx -= 1

    print(cnt)
