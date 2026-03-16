n = int(input())

index = 1
count = 0
while index*index <= n:
    count += 1
    index += 1
print(count)