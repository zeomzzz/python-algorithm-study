import sys

lst = list(sys.stdin.readline().rstrip())
piece = 0 # 쇠막대 조각 수
stack = []

for i in range(len(lst)) :
    if lst[i] == "(" :
        stack.append("(")
    else : # lst[i] == ")"
        if lst[i - 1] == "(" : # 레이저 : 쇠막대 자름 -> 쇠막대 시작점만큼 조각 추가
            stack.pop()
            piece += len(stack)
        else : # 쇠 막대의 끝 : 조각 +1
            stack.pop()
            piece += 1

print(piece)
