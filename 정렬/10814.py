import sys
input = sys.stdin.readline

n = int(input())

lst = []
for i in range(n):
    age, name = input().split()
    lst.append((int(age),i,name))

lst.sort()

for a,i,n in lst:
    print(a, n)