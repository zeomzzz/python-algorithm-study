import sys
input = sys.stdin.readline

l, c = map(int, input().split()) # l : 알파벳 소문자 개수, c : 암호로 사용한 문자의 종류
letters = list(input().split())
letters.sort()

vowels = ["a", "e", "i", "o", "u"]
code = []

def backtracking(idx, cnt) :

    # base case
    if cnt == l :
        vowel = 0
        for x in code :
            if x in vowels : vowel += 1

        if vowel >= 1 and (l - vowel) >= 2 :
            print(''.join(code))

    # recursive (backtracking)
    for i in range(idx, c) :
        code.append(letters[i])
        backtracking(i + 1, cnt + 1)
        code.pop()

backtracking(0, 0)
