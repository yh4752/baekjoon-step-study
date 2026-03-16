# 아이디어. 모든 간격을 동일하게 하기 위해서는 간격들의 최대공약수로 맞춰야한다.

import math

n = int(input())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

arr.sort()

diff = [arr[i+1] - arr[i] for i in range(len(arr) - 1)]

gcd = math.gcd(*diff)

print(((arr[-1] - arr[0]) // gcd) + 1 - len(arr))