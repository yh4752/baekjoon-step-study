import math

x,y,w,h = map(int, input().split())

min_dist = -1

# 왼아 -> 왼위
for i in range(0, h+1):
    dst = math.sqrt(x**2 + (y-i)**2)
    if min_dist == -1 or min_dist > dst:
        min_dist = dst

# 왼위 -> 오위
for i in range(0, w+1):
    dst = math.sqrt((x-i)**2+(y-h)**2)
    if min_dist == -1 or min_dist > dst:
        min_dist = dst

# 오위 -> 오아
for i in range(h, -1, -1):
    dst = math.sqrt((x-w)**2+(y-i)**2)
    if min_dist == -1 or min_dist > dst:
        min_dist = dst

# 오아 -> 왼아
for i in range(w, -1, -1):
    dst = math.sqrt((x-i)**2+y**2)
    if min_dist == -1 or min_dist > dst:
        min_dist = dst

print(int(min_dist))