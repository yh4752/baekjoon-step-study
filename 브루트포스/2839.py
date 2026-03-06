n = int(input())

five = 0
count = 5000
check = 0
while True:
    cn = n - 5*five
    if cn < 0:
        if check == 0:
            count = -1
        break
    if cn % 3 ==0:
        three = cn // 3
        if five+three < count:
            count = five + three
            check += 1
    five += 1
print(count)