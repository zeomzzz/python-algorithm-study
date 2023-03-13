import sys

n = int(sys.stdin.readline().rstrip())
wines = [0]
w = 0

for i in range(1, n + 1) :
    ww = w # ww : 이전에 담은 wine 양
    w = int(sys.stdin.readline().rstrip()) # w : 새로 담은 와인의 양

    # 첫번째 와인은 바로 wines에 추가
    if i == 1 :
        wines.append(w)
    # 두번째의 최대값은 첫번째 + 두번째
    elif i == 2 :
        wines.append(wines[1] + w)
    # 세 잔의 와인 이용해서 나오는 세 가지 경우 중 최대값
    elif i == 3 :
        tmp = [wines[2], wines[1] + w, ww + w]
        wines.append(max(tmp))
    # 그 외
    # w을 마시고 ww 안 마시는 경우 : wines[i - 2] + w
    # w을 마시고 ww도 마시는 경우 : wines[i - 3] + ww + w
    # w 안 마시는 경우 : wines[i - 1]
    else :
        tmp = [wines[i - 1], wines[i - 2] + w, wines[i - 3] + ww + w]
        wines.append(max(tmp))

# wines의 마지막 요소를 출력
print(wines[-1])
