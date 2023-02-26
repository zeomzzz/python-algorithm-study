import sys

h = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
h.sort()
n = sum(h) - 100 # 합이 9난쟁이 키의 합 - 100 인 두 난쟁이를 찾음

for i in range(8) :
    for j in range(i + 1, 9) :
        if h[j] < n and h[i] + h[j] == n : # 두 난쟁이의 키의 합이 n이려면 한 난쟁이의 키가 n보다 클 수 없음
            h.remove(h[j])
            h.remove(h[i])
            break

    if len(h) == 7 : # 난쟁이 키 제거되어서 7난쟁이만 남았을 때 종료
        break

for i in h :
    print(i)
