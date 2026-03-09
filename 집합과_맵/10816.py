n = int(input())

check_list = list(map(int, input().split()))

check_dict = {}
for check in check_list:
    if check not in check_dict:
        check_dict[check] = 1
    else:
        check_dict[check] += 1

m = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    if num in check_dict:
        print(check_dict[num], end=" ")
    else:
        print(0, end=" ")
