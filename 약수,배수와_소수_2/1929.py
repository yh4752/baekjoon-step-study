import math

a, b = map(int, input().split())

def is_prime(a):
    if a < 2:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

for i in range(a, b+1):
    if is_prime(i):
        print(i)