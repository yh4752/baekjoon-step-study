import sys
input = sys.stdin.readline
# 시간초과가 나오면 일단 import sys
n = int(input())

stack = []
for _ in range(n):
    cmd = input().split()

    num = 0
    if len(cmd) == 2:
        num = int(cmd[1])
        cmd = int(cmd[0])
    else:
        cmd = int(cmd[0])

    if cmd == 1:
        stack.append(num)
    elif cmd == 2:
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif cmd == 3:
        print(len(stack))
    elif cmd == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    else:
        continue