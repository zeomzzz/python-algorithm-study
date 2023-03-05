n = int(input()) # 단어의 개수

words = [[] for _ in range(51)]  # 문자열의 길이 1 ~ 50 각 인덱스에서 저장

for _ in range(n) :
    word = input()
    l = len(word)
    words[l].append(word)

for i in words :
    if len(i) > 0 :
        if len(i) > 1 :
            i = list(set(i))
            i.sort()

        for k in i :
            print(k)
