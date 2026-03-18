import sys
input = sys.stdin.readline

n = int(input())

line = list(map(int, input().split()))
line.reverse()

wait = []

index = 1

while True:
    if line and not wait:
        if line[-1] != index:
            wait.append(line.pop())
        else:
            line.pop()
            index += 1
    elif line and wait:
        if line[-1] == index:
            line.pop()
            index += 1
        elif wait[-1] == index:
            wait.pop()
            index += 1
        elif line[-1] != index:
            wait.append(line.pop())

    elif not line and wait:
        if wait[-1] == index:
            wait.pop()
            index += 1
        else:
            print("Sad")
            break
    elif not line and not wait:
        print("Nice")
        break