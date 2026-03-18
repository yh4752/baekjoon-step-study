import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
line.reverse()

wait = []
target = 1

while line or wait:
    if wait and wait[-1] == target:
        wait.pop()
        target += 1
    elif line and line[-1] == target:
        line.pop()
        target += 1
    elif line:
        wait.append(line.pop())
    else:
        print("Sad")
        break
else:
    print("Nice")