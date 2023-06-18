import sys
from collections import deque
input = sys.stdin.readline

S, P = map(int, input().rstrip().split()) # dna의 길이 S, 부분문자열의 길이 P
dna = input().rstrip()
A, C, G, T = map(int, input().rstrip().split())

cnt = 0

# 첫번째 문자열 확인
part = deque()
a, c, g, t = 0, 0, 0, 0
for i in range(P) :
    part.append(dna[i])

    match dna[i] :
        case 'A' :
            a += 1
        case 'C' :
            c += 1
        case 'G' :
            g += 1
        case 'T' :
            t += 1

if a >= A and c >= C and g >= G and t >= T :
    cnt += 1

end = P
while end < S :
    popped = part.popleft()
    appended = dna[end]
    part.append(appended)

    match popped :
        case 'A' :
            a -= 1
        case 'C' :
            c -= 1
        case 'G' :
            g -= 1
        case 'T' :
            t -= 1

    match appended :
        case 'A' :
            a += 1
        case 'C' :
            c += 1
        case 'G' :
            g += 1
        case 'T' :
            t += 1

    if a >= A and c >= C and g >= G and t >= T:
        cnt += 1

    end += 1

print(cnt)
