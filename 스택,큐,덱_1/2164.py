import collections
n = int(input())

deque = collections.deque()

for i in range(1,n+1):
    deque.append(i)

while len(deque) != 1:
    deque.popleft()
    deque.append(deque.popleft())
else:
    print(deque[0])