# get 활용해서 풀기
n = int(input())

check_list = list(map(int, input().split()))

check_dict = {}
for check in check_list:
    check_dict[check] = check_dict.get(check, 0) + 1

m = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    print(check_dict.get(num, 0), end=" ")
