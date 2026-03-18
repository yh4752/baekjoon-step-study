import collections

deque = collections.deque()

n, k = map(int, input().split())

for i in range(1, n+1):
    deque.append(i)
result = []

while deque:
    for _ in range(k-1):
        deque.append(deque.popleft())

    result.append(deque.popleft())


print(f"<{', '.join(map(str,result))}>")