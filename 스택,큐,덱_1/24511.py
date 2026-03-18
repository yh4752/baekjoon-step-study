import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = int(input())
nums = list(map(int, input().split()))
result = []

# 세팅
q = deque()
for i in range(n):
    if a[i] == 0:
        q.appendleft(b[i])

for num in nums:
    q.append(num)
    result.append(q.popleft())
print(' '.join(map(str,result)))