import sys

def solution(N, M, Arr) :
    ans = []
    arr = sorted(Arr)

    if M == 1 :
        for i in arr :
            if len(ans) == 0 :
                ans.append([i])
            else :
                if ans[-1] != [i] :
                    ans.append([i])
    else :
        for i in solution(N, M-1, Arr) :

            # 새로운 것만 추가하기 위해서 기존 리스트에 있는 것은 제외한 리스트 만듦
            tmp_arr = arr[:]
            for j in i :
                tmp_arr.remove(j)

            # 새로운 것을 추가하여 답 리스트에 추가
            # 비내림차순이므로 답 리스트 마지막 수보다 새로운 수가 크거가 같은 경우에만 추가
            # 그런데 이전에 추가한 것과 동일하지 않은 경우에만 추가
            for k in tmp_arr :
                tmp_i = i[:]
                if len(tmp_i) > 0 and tmp_i[-1] <= k :
                    tmp_i.append(k)

                    if len(ans) == 0 :
                        ans.append(tmp_i)
                    else :
                        if tmp_i != ans[-1] :
                            ans.append(tmp_i)

    return ans


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in solution(n, m, arr) :
    i_tmp = list(map(str, i))
    print(' '.join(i_tmp))
