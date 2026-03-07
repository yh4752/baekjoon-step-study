import sys
input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))
sorted_num_list = sorted(num_list)

num_dict = {}

index = 0
for sn in sorted_num_list:
    if sn not in num_dict:
        num_dict[sn] = index
        index += 1

for n in num_list:
    print(num_dict[n], end=' ')