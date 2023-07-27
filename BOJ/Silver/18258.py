import sys
from collections import deque
input = sys.stdin.readline

q = deque()
N = int(input().rstrip())

for i in range(N) :
    cmds = list(input().rstrip().split())
    cmd = cmds[0]

    match cmd :
        case 'push' :
            X = int(cmds[1])
            q.append(X)

        case 'pop' :
            if q : print(q.popleft())
            else : print(-1)

        case 'size' :
            print(len(q))

        case 'empty' :
            if q : print(0)
            else : print(1)

        case 'front' :
            if not q : print(-1)
            else :
                tmp = q.popleft()
                print(tmp)
                q.appendleft(tmp)

        case 'back' :
            if not q : print(-1)
            else :
                tmp = q.pop()
                print(tmp)
                q.append(tmp)
