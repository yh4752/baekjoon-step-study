while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    longest = max(a,b,c)
    remain_sum = a+b+c - longest
    if longest >= remain_sum:
        print("Invalid")
        continue
    toSet = set()
    toSet.add(a)
    toSet.add(b)
    toSet.add(c)
    if len(toSet) == 1:
        print("Equilateral")
    elif len(toSet) == 2:
        print("Isosceles")
    else:
        print("Scalene")