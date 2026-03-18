import sys
import collections
input = sys.stdin.readline

n = int(input())
q = collections.deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == '1':
        q.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        q.append(int(cmd[1]))
    elif cmd[0] == '3':
        print(q.popleft() if q else -1)
    elif cmd[0] == '4':
        print(q.pop() if q else -1)
    elif cmd[0] == '5':
        print(len(q))
    elif cmd[0] == '6':
        print(0 if q else 1)
    elif cmd[0] == '7':
        print(q[0] if q else -1)
    elif cmd[0] == '8':
        print(q[-1] if q else -1)