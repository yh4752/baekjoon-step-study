# Set으로 풀기
import sys
input = sys.stdin.readline

n = int(input())

words = set()

for _ in range(n):
    words.add(input().strip())

words.sort(key=lambda x: (len(x), x))

for w in words:
    print(w)