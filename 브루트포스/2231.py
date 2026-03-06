n = int(input())

num = 1
while True:
    result = 0
    result += num
    copy_num = num
    while copy_num != 0:
        result += copy_num % 10
        copy_num //= 10
    
    if result == n:
        print(num)
        break
    num += 1
    if num > 1000000:
        print(0)
        break