# 최소 공배수 = (a x b) / 최대 공약수(a,b)
"""
최대 공약수 구하는 공식은 암기!! 유클리드 호제법
"""
n = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(n):
    a, b = map(int, input().split())
    lcm = a * b // gcd(a,b)
    print(lcm)
