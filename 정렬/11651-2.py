# sort 함수에 lambda 사용하기
import sys

n = int(sys.stdin.readline())

lst = [tuple(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x: (x[1], x[0]))

for x,y in lst:
    print(x, y)