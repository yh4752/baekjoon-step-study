import sys
input = sys.stdin.readline

result = []
while True:
    line = input().rstrip()

    if len(line) == 1 and line[0] == '.':
        print("\n".join(result))
        break
    else:
        index = 0
        blanket = []
        while line[index] != '.':
            if line[index] == '(':
                blanket.append('(')
            elif line[index] == ')':
                if blanket and blanket[-1] == '(':
                    blanket.pop()
                else:
                    blanket.append(')')
                    break
            elif line[index] == '[':
                blanket.append('[')
            elif line[index] == ']':
                if blanket and blanket[-1] == '[':
                    blanket.pop()
                else:
                    blanket.append(']')
                    break
            index += 1

        if blanket:
            result.append("no")
        else:
            result.append("yes")