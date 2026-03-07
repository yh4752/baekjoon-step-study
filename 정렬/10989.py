# Counting Sort 방식
import sys
n = int(sys.stdin.readline())

arr = [0]*10001
for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1

index = 1
count = 1
while index <= n:
    for i in range(arr[count]):
        print(count)
        index += 1
    count += 1