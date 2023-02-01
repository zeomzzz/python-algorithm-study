import sys

N = int(sys.stdin.readline())

deque = []

for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "push_front":
        deque.insert(0, cmd[1])
    elif cmd[0] == "push_back":
        deque.append(cmd[1])
    elif cmd[0] == "pop_front":
        if len(deque) > 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if len(deque) > 0:
            print(deque.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(deque) > 0:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if len(deque) > 0:
            print(deque[-1])
        else:
            print(-1)
