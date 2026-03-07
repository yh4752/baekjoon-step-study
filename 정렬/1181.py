import sys

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s not in lst:
        lst.append((len(s), s))

lst = sorted(list(set(lst)))

for l, w in lst:
    print(w)
