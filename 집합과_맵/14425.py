import sys
input = sys.stdin.readline

n,m = map(int, input().split())

words_set = set()
for _ in range(n):
    s = input()
    words_set.add(s)

count = 0 
for _ in range(m):
    s = input()
    if s in words_set:
        count+=1

print(count)