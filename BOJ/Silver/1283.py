import sys
input = sys.stdin.readline

N = int(input().rstrip())

visited = [0] * 26

for _ in range(N) :
    options = input().rstrip()
    option = options.split()
    result = ""

    flag = False

    if len(option) == 0 :
        flag = True
        print(options)

    # 1. 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다
    for word in option :
        if not flag :
            tmp = word.lower()

            if visited[ord(tmp[0]) - ord('a')] == 0 : # 아직 단축키 지정 안함
                visited[ord(tmp[0]) - ord('a')] = 1 # 단축키 지정
                result += ("[" + word[0] + "]" + word[1:] + " ")
                flag = True
            else :
                result += (word + " ")
        else :
            result += (word + " ")

    if flag :
        result = result.rstrip()
        print(result)
    else : # 첫 글자로는 단축키 지정 못함
        # 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정
        result = ""

        for i in range(len(options)) :
            if not flag :
                if options[i] == " " :
                    result += options[i]
                else :
                    tmp = options[i].lower()

                    if visited[ord(tmp) - ord('a')] == 0 : # 아직 단축키 지정 안함
                        visited[ord(tmp) - ord('a')] = 1
                        result += ("[" + options[i] + "]")
                        flag = True
                    else :
                        result += options[i]
            else :
                result += options[i:]
                break

        print(result)
