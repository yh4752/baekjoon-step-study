# 기존 코드와 유사하나 조금 더 간결하게 작성

while True:
    a,b,c = map(int, input().split())

    if a == b == c == 0:
        break

    longest = max(a,b,c)
    if longest >= a+b+c-longest:
        print("Invalid")
        continue

    s = len({a,b,c})

    if s == 1:
        print("Equilateral")
    elif s == 2:
        print("Isosceles")
    else:
        print("Scalene")