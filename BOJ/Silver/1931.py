import sys
input = sys.stdin.readline

N = int(input().rstrip())
times = [list(map(int, input().rstrip().split())) for _ in range(N)]
times.sort(key=lambda  x : (x[1], x[0]))

rooms = [times[0]]
prev = times[0][1]

for i in range(1, N) :
    if times[i][0] >= prev :
        rooms.append(times[i])
        prev = times[i][1]

print(len(rooms))
