import sys
input = sys.stdin.readline

n = int(input())

result = []
for _ in range(n):
    line = input().strip()

    stack = []
    
    for l in line:
        if l == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                stack.append(")")
                break

    if stack:
        result.append("NO")
    else:
        result.append("YES")

print("\n".join(result))