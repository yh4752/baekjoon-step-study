import math

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

bunmo = a2*b2 // math.gcd(a2, b2)

a1 = a1 * (bunmo // a2)
b1 = b1 * (bunmo // b2)

bunja = a1 + b1

g = math.gcd(bunja, bunmo) # 기약분수로 만들기

print(bunja // g, bunmo // g)
