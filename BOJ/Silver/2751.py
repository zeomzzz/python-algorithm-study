# 리스트를 숫자 개수만큼의 크기로 만들고 저장
import sys

n = int(sys.stdin.readline().rstrip())
lst = [0] * n

for i in range(n) :
    lst[i] = int(sys.stdin.readline().rstrip())

lst.sort()

print(*lst, sep='\n')


# 입력 받을 때마다 리스트에 추가
import sys

n = int(sys.stdin.readline().rstrip())
lst = []

for i in range(n) :
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()

print(*lst, sep='\n')
