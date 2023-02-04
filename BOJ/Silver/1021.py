import sys

# N : 큐의 크기, M : 뽑아 내려는 수의 개수
N, M = map(int, sys.stdin.readline().rstrip().split())
# pop_lst : 뽑아 내려는 수의 리스트
pop_lst = list(map(int, sys.stdin.readline().rstrip().split()))
# 큐 생성
queue = [0] * N
for i in range(N):
    queue[i] += i + 1

cnt = 0

while len(pop_lst) > 0:

    while queue[0] != pop_lst[0]:

        if queue.index(pop_lst[0]) < len(queue) / 2:
            queue.append(queue.pop(0))  # move left
            cnt += 1
        else:
            queue.insert(0, queue.pop())  # move right
            cnt += 1

    queue.pop(0)
    pop_lst.pop(0)

print(cnt)
