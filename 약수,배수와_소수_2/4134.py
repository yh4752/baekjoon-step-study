import math
n = int(input())

def check_prime(c):
    if c < 2:
        return False
    for i in range(2, int(math.sqrt(c)) + 1):
        if c % i == 0:
            return False
    return True

def next_prime(a):
    if a <= 2:
        return 2
    if a % 2 == 0:
        a += 1
    while True:
        if check_prime(a):
            return a
        else:
            a += 1


for _ in range(n):
    a = int(input())
    print(next_prime(a))