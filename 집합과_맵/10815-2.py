# 존재 여부를 확인할 때는 set을 사용하자.

import sys
input = sys.stdin.readline

n = int(input())
check_set = set(map(int, input().split()))

m = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    if num in check_set:
        print("1", end=" ")
    else:
        print("0", end=" ")