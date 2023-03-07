import sys

word = sys.stdin.readline().rstrip()
letter = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in letter :
    word = word.replace(i, "a")

print(len(word))
