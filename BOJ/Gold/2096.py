import sys
input = sys.stdin.readline

N = int(input())  # N줄에 거쳐서 입력

dp_max = [0, 0, 0]
dp_min = [0, 0, 0]

for i in range(N) :
    if i == 0 :
        dp_max = list(map(int, input().split()))
        dp_min = dp_max[:]
    else :
        graph = list(map(int, input().split()))
        dp_max[0] = max(dp_max[0], dp_max[1]) + graph[0]
        dp_min[0] = min(dp_min[0], dp_min[1]) + graph[0]

        dp_max[2] = max(dp_max[1], dp_max[2]) + graph[2]
        dp_min[2] = min(dp_min[1], dp_min[2]) + graph[2]

        dp_max[1] = max(dp_max[0] - graph[0], dp_max[2] - graph[2]) + graph[1]
        dp_min[1] = min(dp_min[0] - graph[0], dp_min[2] - graph[2]) + graph[1]

print(str(max(dp_max)) + " " + str(min(dp_min)))
