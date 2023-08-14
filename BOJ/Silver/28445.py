import sys
input = sys.stdin.readline

colors = []
colors += input().rstrip().split(" ")
colors += input().rstrip().split(" ")
colors = list(set(colors))
colors.sort()

for body in colors :
    for tail in colors :
        print(body + " " + tail)
