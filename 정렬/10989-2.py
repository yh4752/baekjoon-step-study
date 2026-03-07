# 좀 더 빠른 방식
import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
arr = [0]*10001

for _ in range(n):
    arr[int(input())] += 1

for i in range(1,10001):
    for _ in range(arr[i]):
        write(str(i) + "\n")