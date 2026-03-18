import collections
import sys
input = sys.stdin.readline

n = int(input())
result = []

q = collections.deque()

for i in range(1,n+1):
    q.append(i)

cmd = list(map(int, input().split()))
ballons = dict()

index = 1
for c in cmd:
    ballons[index] = c
    index += 1

# 1번 터트리기
result.append(1)
num = ballons[q.popleft()]
start = 0

while q:
    if num > 0:
        for _ in range(num-1):
            q.append(q.popleft())
    else:
        num = -1 * num
        for _ in range(num):
            q.appendleft(q.pop())
    bnum = q.popleft()
    num = ballons[bnum]
    result.append(bnum)

print(' '.join(map(str,result)))