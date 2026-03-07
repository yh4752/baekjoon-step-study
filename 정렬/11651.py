import sys

n = int(sys.stdin.readline())

# lst = [tuple(map(int,input().split())) for _ in range(n)]
lst = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((b,a))

lst.sort()
for y,x in lst:
    print(x,y)