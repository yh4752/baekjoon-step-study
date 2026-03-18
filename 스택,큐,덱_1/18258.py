import sys
import collections
input = sys.stdin.readline

n = int(input())

deque = collections.deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        num = int(cmd[1])
        deque.append(num)

    elif cmd[0] == "pop":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        print(1 if deque else 0)
    elif cmd[0] == "front":
        print(deque[0] if deque else -1)
    elif cmd[0] == "back":
        print(deque[-1] if deque else -1)