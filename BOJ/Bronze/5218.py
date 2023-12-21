n = int(input())

for _ in range(n):
	s = []
	word1, word2 = map(list, input().split())
	for i in range(len(word1)):
		if ord(word1[i]) <= ord(word2[i]): s.append(ord(word2[i]) - ord(word1[i]))
		else: s.append(ord(word2[i]) + 26 - ord(word1[i]))
	print('Distances: ', end ='')
	for i in s: print(i, end=' ')
	print()
