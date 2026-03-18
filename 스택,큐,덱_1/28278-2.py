import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == '1':
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':
        if stack:
            result.append(str(stack.pop()))
        else:
            result.append('-1')
    elif cmd[0] == '3':
        result.append(str(len(stack)))
    elif cmd[0] == '4':
        result.append('0' if stack else '1')
    elif cmd[0] == '5':
        if stack:
            result.append(str(stack[-1]))
        else:
            result.append('-1')

print('\n'.join(result))