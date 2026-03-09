import sys
input = sys.stdin.readline

n = int(input())
check_list = list(map(int, input().split()))

m = int(input())
num_list = list(map(int, input().split()))

num_dict = {}
for num in num_list:
    num_dict[num] = 0
for check in check_list:
    if check in num_dict:
        num_dict[check] = 1

for num in num_list:
    print(num_dict[num], end=" ")